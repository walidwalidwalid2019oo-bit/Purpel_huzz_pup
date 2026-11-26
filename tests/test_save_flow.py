import ast
import unittest
from pathlib import Path


def dotted_name(node):
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
        return ".".join(reversed(parts))
    return None


def is_string_equality(node, left, value):
    return (
        isinstance(node, ast.Compare)
        and len(node.ops) == 1
        and isinstance(node.ops[0], ast.Eq)
        and dotted_name(node.left) == left
        and isinstance(node.comparators[0], ast.Constant)
        and node.comparators[0].value == value
    )


class SaveFlowTests(unittest.TestCase):
    def test_escape_pause_saves_before_returning_to_menu(self):
        source = Path(__file__).resolve().parents[1] / "main.py"
        tree = ast.parse(source.read_text(encoding="utf-8"))
        main_function = next(
            node for node in tree.body
            if isinstance(node, ast.FunctionDef) and node.name == "main"
        )
        escape_handler = next(
            node for node in ast.walk(main_function)
            if isinstance(node, ast.If)
            and is_string_equality(node.test, "event.key", "pygame.K_ESCAPE")
        )
        dialogue_handler = escape_handler.body[0]
        self.assertIsInstance(dialogue_handler, ast.If)
        play_branch = dialogue_handler.orelse[0]
        self.assertIsInstance(play_branch, ast.If)
        self.assertTrue(is_string_equality(play_branch.test, "game_state", "play"))

        save_index = next(
            index for index, node in enumerate(play_branch.body)
            if isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Name)
            and node.value.func.id == "save_game"
        )
        menu_index = next(
            index for index, node in enumerate(play_branch.body)
            if isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "game_state"
                    for target in node.targets)
            and isinstance(node.value, ast.Constant)
            and node.value.value == "menu"
        )
        self.assertLess(save_index, menu_index)


if __name__ == "__main__":
    unittest.main()
