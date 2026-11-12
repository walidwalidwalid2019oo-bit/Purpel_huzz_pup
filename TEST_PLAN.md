# PURPLE HAZE — Test Plan

## Every change
- [ ] Python syntax check passes.
- [ ] Game starts from a clean launch.
- [ ] No traceback appears during the tested flow.
- [ ] Keyboard and touch controls both work where applicable.
- [ ] HUD remains readable at phone aspect ratios.
- [ ] Existing progress is not silently reset.

## Player movement
- [ ] Move left and right on every platform.
- [ ] Jump from ground and platform edges.
- [ ] Land on platforms without falling through.
- [ ] Dash respects cooldown.
- [ ] Falling respawns safely and health behaves as intended.

## Interactions
- [ ] ECHO dialogue advances and closes correctly.
- [ ] Outpost reward is granted only once.
- [ ] Cave reward is granted only once.
- [ ] Portal remains locked while shards are missing.
- [ ] Portal completion triggers only when requirements are met.

## Inventory and shop
- [ ] Shards increment the correct item count.
- [ ] Veil Coins update correctly.
- [ ] Purchases fail safely when funds are insufficient.
- [ ] Owned weapons cannot be charged for twice.
- [ ] Equipping an owned weapon updates the selected weapon.
- [ ] Inventory and shop panels open and close correctly.

## Android acceptance
- [ ] GitHub Actions completes successfully.
- [ ] APK artifact exists and is downloadable.
- [ ] APK installs on a real Android device.
- [ ] Game launches in landscape orientation.
- [ ] Touch controls are reachable and responsive.
- [ ] App can be closed and reopened without a crash.
- [ ] Performance is acceptable on the target phone.

A syntax check is not a game test. A successful CI build is not proof of correct behavior on every device.
