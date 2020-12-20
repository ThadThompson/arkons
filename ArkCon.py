"""
ARK RCON Scripts

Using RCON client: https://github.com/pmrowla/pysrcds
"""
from srcds.rcon import RconConnection

THAD = 200830874
BRAYDEN = 906339131
MALCOLM = 625791640
ZANE = 791449563
BO = 575127110

SAM = 203674606
ATTICUS = 714818910

TRIBE_PLAYERS = [
    THAD, BO, MALCOLM, ZANE
]

# Elements
ELEMENT = "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Element.PrimalItemResource_Element'"

ITEMS = {
    'METAL_HATCHET':               "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponMetalHatchet.PrimalItem_WeaponMetalHatchet'",
    'METAL_PICK':                  "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponMetalPick.PrimalItem_WeaponMetalPick'",
    'METAL_SICKLE':                "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponSickle.PrimalItem_WeaponSickle'",
    'TORCH':                       "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponTorch.PrimalItem_WeaponTorch'",
    'GPS':                         "Blueprint'/Game/PrimalEarth/Test/PrimalItem_WeaponGPS.PrimalItem_WeaponGPS'",
    'PARACHUTE':                   "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/BaseBPs/PrimalItemConsumableBuff_Parachute.PrimalItemConsumableBuff_Parachute'",
    'HANDCUFFS':                   "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponHandcuffs.PrimalItem_WeaponHandcuffs'",

    'C4_DETONATOR':                "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponC4.PrimalItem_WeaponC4'",
    'IED':                         "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponTripwireC4.PrimalItem_WeaponTripwireC4'",
    'OIL_JAR':                     "Blueprint'/Game/ScorchedEarth/WeaponOilJar/PrimalItem_WeaponOilJar.PrimalItem_WeaponOilJar'",
    'NARCOTIC_TRAP':               "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponPoisonTrap.PrimalItem_WeaponPoisonTrap'",
    'PLANT_Y_TRAP':                "Blueprint'/Game/ScorchedEarth/WeaponPlantSpeciesY/PrimalItemStructure_PlantSpeciesYTrap.PrimalItemStructure_PlantSpeciesYTrap'",

    'POISON_GRENADE':              "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_PoisonGrenade.PrimalItem_PoisonGrenade'",

    'BOOMERANG':                   "Blueprint'/Game/ScorchedEarth/WeaponBoomerang/PrimalItem_WeaponBoomerang.PrimalItem_WeaponBoomerang'",
    'BEAR_TRAP':                   "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_BearTrap.PrimalItemStructure_BearTrap'",
    'BOLA':                        "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponBola.PrimalItem_WeaponBola'",

    'BOW':                         "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponBow.PrimalItem_WeaponBow'",
    'CROSSBOW':                    "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponCrossbow.PrimalItem_WeaponCrossbow'",
    'COMPOUND_BOW':                "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponCompoundBow.PrimalItem_WeaponCompoundBow'",

    'LANCE':                       "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponLance.PrimalItem_WeaponLance'",
    'WHIP':                        "Blueprint'/Game/ScorchedEarth/WeaponWhip/PrimalItem_WeaponWhip.PrimalItem_WeaponWhip'",
    'SPEAR':                       "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponSpear.PrimalItem_WeaponSpear'",
    'SWORD':                       "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponSword.PrimalItem_WeaponSword'",
    'ELECTRIC_PROD':               "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponProd.PrimalItem_WeaponProd'",

    'ASSAULT_RIFLE':               "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponRifle.PrimalItem_WeaponRifle'",
    'SHOTGUN':                     "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponShotgun.PrimalItem_WeaponShotgun'",
    'LONGNECK_RIFLE':              "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponOneShotRifle.PrimalItem_WeaponOneShotRifle'",
    'SNIPER_RIFLE':                "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponMachinedSniper.PrimalItem_WeaponMachinedSniper'",

    'C4':                          "Blueprint'/Game/PrimalEarth/Test/PrimalItemC4Ammo.PrimalItemC4Ammo'",

    'STONE_ARROW':                 "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_ArrowStone.PrimalItemAmmo_ArrowStone'",
    'TRANQ_ARROW':                 "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_ArrowTranq.PrimalItemAmmo_ArrowTranq'",
    'FLAME_ARROW':                 "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_ArrowFlame.PrimalItemAmmo_ArrowFlame'",

    'SIMPLE_RIFLE_AMMO':           "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_SimpleRifleBullet.PrimalItemAmmo_SimpleRifleBullet'",
    'SIMPLE_SHOTGUN_AMMO':         "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_SimpleShotgunBullet.PrimalItemAmmo_SimpleShotgunBullet'",

    'ADVANCED_BULLET':             "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_AdvancedBullet.PrimalItemAmmo_AdvancedBullet'",
    'ADVANCED_RIFLE_AMMO':         "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_AdvancedRifleBullet.PrimalItemAmmo_AdvancedRifleBullet'",
    'ADVANCED_SNIPER_AMMO':        "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_AdvancedSniperBullet.PrimalItemAmmo_AdvancedSniperBullet'",

    'TRANQ_DART':                  "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_TranqDart.PrimalItemAmmo_TranqDart'",
    'SHOCKING_TRANQ_DART':         "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_RefinedTranqDart.PrimalItemAmmo_RefinedTranqDart'",

    # Armor
    'HIDE_HELMET':                 "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemArmor_HideHelmet.PrimalItemArmor_HideHelmet'",
    'HIDE_SHIRT':                  "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemArmor_HideShirt.PrimalItemArmor_HideShirt'",
    'HIDE_PANTS':                  "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemArmor_HidePants.PrimalItemArmor_HidePants'",
    'HIDE_GLOVES':                 "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemArmor_HideShirt.PrimalItemArmor_HideShirt'",
    'HIDE_BOOTS':                  "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemArmor_HideBoots.PrimalItemArmor_HideBoots'",

    'METAL_HELMET':                "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Metal/PrimalItemArmor_MetalHelmet.PrimalItemArmor_MetalHelmet'",
    'METAL_SHIRT':                 "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Metal/PrimalItemArmor_MetalShirt.PrimalItemArmor_MetalShirt'",
    'METAL_PANTS':                 "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Metal/PrimalItemArmor_MetalPants.PrimalItemArmor_MetalPants'",
    'METAL_GLOVES':                "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Metal/PrimalItemArmor_MetalGloves.PrimalItemArmor_MetalGloves'",
    'METAL_BOOTS':                 "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Metal/PrimalItemArmor_MetalBoots.PrimalItemArmor_MetalBoots'",

    'FUR_HELMET':                  "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Fur/PrimalItemArmor_FurHelmet.PrimalItemArmor_FurHelmet'",
    'FUR_SHIRT':                   "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Fur/PrimalItemArmor_FurShirt.PrimalItemArmor_FurShirt'",
    'FUR_PANTS':                   "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Fur/PrimalItemArmor_FurPants.PrimalItemArmor_FurPants'",
    'FUR_GLOVES':                  "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Fur/PrimalItemArmor_FurGloves.PrimalItemArmor_FurGloves'",
    'FUR_BOOTS':                   "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Fur/PrimalItemArmor_FurBoots.PrimalItemArmor_FurBoots'",

    'GHILLIE_HELMET':              "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Ghillie/PrimalItemArmor_GhillieHelmet.PrimalItemArmor_GhillieHelmet'",
    'GHILLIE_SHIRT':               "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Ghillie/PrimalItemArmor_GhillieShirt.PrimalItemArmor_GhillieShirt'",
    'GHILLIE_PANTS':               "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Ghillie/PrimalItemArmor_GhilliePants.PrimalItemArmor_GhilliePants'",
    'GHILLIE_GLOVES':              "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Ghillie/PrimalItemArmor_GhillieGloves.PrimalItemArmor_GhillieGloves'",
    'GHILLIE_BOOTS':               "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Ghillie/PrimalItemArmor_GhillieBoots.PrimalItemArmor_GhillieBoots'",

    # Structures
    'AUTO_TURRET':                 "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Turret.PrimalItemStructure_Turret'",
    'HEAVY_AUTO_TURRET':           "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_HeavyTurret.PrimalItemStructure_HeavyTurret'",

    'WOODEN_CAGE':                 "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodCage.PrimalItemStructure_WoodCage'",

    'ELECTRIC_GENERATOR':          "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerGenerator.PrimalItemStructure_PowerGenerator'",
    'ELECTRIC_OUTLET':             "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerOutlet.PrimalItemStructure_PowerOutlet'",
    'ELECTRIC_CABLE_INTERSECTION': "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerCableIntersection.PrimalItemStructure_PowerCableIntersection'",
    'ELECTRIC_CABLE_STRAIGHT':     "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerCableStraight.PrimalItemStructure_PowerCableStraight'",
    'ELECTRIC_CABLE_FLEX':         "Blueprint'/Game/PrimalEarth/StructuresPlus/Wires/Flex/PrimalItemStructure_Wire_Flex.PrimalItemStructure_Wire_Flex'",
    'ELECTRIC_CABLE_INCLINED':     "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerCableIncline.PrimalItemStructure_PowerCableIncline'",
    'ELECTRIC_CABLE_VERTICAL':     "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerCableVertical.PrimalItemStructure_PowerCableVertical'",

    # Tek
    'TEK_BOOTS':                   "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/TEK/PrimalItemArmor_TekBoots.PrimalItemArmor_TekBoots'",
    'TEK_PANTS':                   "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/TEK/PrimalItemArmor_TekPants.PrimalItemArmor_TekPants'",
    'TEK_SHIRT':                   "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/TEK/PrimalItemArmor_TekShirt.PrimalItemArmor_TekShirt'",
    'TEK_GLOVES':                  "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/TEK/PrimalItemArmor_TekGloves.PrimalItemArmor_TekGloves'",
    'TEK_HELMET':                  "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/TEK/PrimalItemArmor_TekHelmet.PrimalItemArmor_TekHelmet'",
    'TEK_GRENADE':                 "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_TekGrenade.PrimalItem_TekGrenade'",
    'TEK_GRAVITY_GRENADE':         "Blueprint'/Game/Extinction/CoreBlueprints/Weapons/PrimalItem_WeaponTekGravityGrenade.PrimalItem_WeaponTekGravityGrenade'",
    'TEK_RIFLE':                   "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_TekRifle.PrimalItem_TekRifle'",
    'TEK_SWORD':                   "Blueprint'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponTekSword.PrimalItem_WeaponTekSword'",
    'TEK_SHOULDER_CANNON':         "Blueprint'/Game/Genesis/Items/Armor/PrimalItemArmor_ShoulderCannon.PrimalItemArmor_ShoulderCannon'",
    'TEK_SHIELD':                  "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Shields/PrimalItemArmor_ShieldTek.PrimalItemArmor_ShieldTek'",

    # Saddles
    'ARGENTAVIS':                  "Blueprint'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemArmor_ArgentavisSaddle.PrimalItemArmor_ArgentavisSaddle'",

    # Resources
    'STONE':                       "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Stone.PrimalItemResource_Stone'",
    'THATCH':                      "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Thatch.PrimalItemResource_Thatch'",
    'WOOD':                        "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Wood.PrimalItemResource_Wood'",
    'HIDE':                        "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Hide.PrimalItemResource_Hide'",
    'FLINT':                       "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Flint.PrimalItemResource_Flint'",
    'FIBER':                       "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Fibers.PrimalItemResource_Fibers'",

    'OBSIDIAN':                    "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Obsidian.PrimalItemResource_Obsidian'",
    'CRYSTAL':                     "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Crystal.PrimalItemResource_Crystal'",

    'METAL_INGOT':                 "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_MetalIngot.PrimalItemResource_MetalIngot'",
    'CEMENTING_PASTE':             "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_ChitinPaste.PrimalItemResource_ChitinPaste'",

    'ELECTRONICS':                 "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Electronics.PrimalItemResource_Electronics'",
    'POLYMER':                     "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Polymer.PrimalItemResource_Polymer'",
    'GASOLINE':                    "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Gasoline.PrimalItemResource_Gasoline'",
    'GUNPOWDER':                   "Blueprint'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Gunpowder.PrimalItemResource_Gunpowder'",
}


def give(pid: int, item: str, quantity: int, quality):
    return f'GiveItemToPlayer {pid} "{ITEMS[item]}" {quantity} {quality} 0'


def join_tribe(pid: int, name: str):
    return f'ForcePlayerToJoinTribe {pid} {name}'


# def primitive_loadout(id):
#     return [
#        # f'ClearPlayerInventory {id} 1 1 1',
#         give(id, HIDE_BOOTS,  1, 8),
#         give(id, HIDE_PANTS,  1, 8),
#         give(id, HIDE_SHIRT,  1, 8),
#         give(id, HIDE_GLOVES, 1, 8),
#         give(id, HIDE_HELMET, 1, 8),
#
#         give(id, METAL_HATCHET, 1, 20),
#         give(id, METAL_PICK, 1, 20),
#         give(id, METAL_SICKLE, 1, 20),
#
#         give(id, BOLA, 4, 20),
#         give(id, WHIP, 1, 20),
#         give(id, BOOMERANG, 5, 10),
#         give(id, BOW, 1, 20),
#         give(id, SPEAR, 4, 20),
#         give(id, STONE_ARROW, 100, 20)
#     ]


# def setup_tek(id):
#     return [
#        # f'ClearPlayerInventory {id} 1 1 1',
#         give(id, TEK_BOOTS,  1, 20),
#         give(id, TEK_PANTS,  1, 20),
#         give(id, TEK_SHIRT,  1, 20),
#         give(id, TEK_GLOVES, 1, 20),
#         give(id, TEK_HELMET, 1, 20),
#
#         give(id, TEK_RIFLE, 1, 20),
#         give(id, TEK_SWORD, 1, 20),
#         give(id, TEK_SHOULDER_CANNON, 1, 20),
#         give(id, TEK_SHIELD, 1, 20),
#
#         give(id, TEK_GRENADE, 10, 10),
#         give(id, TEK_GRAVITY_GRENADE, 10, 10),
#         give(id, TEK_GRENADE, 10, 10),
#         give(id, TEK_GRENADE, 10, 10),
#         give(id, ELEMENT, 100, 1),
#         give(id, ELEMENT, 100, 1),
#         give(id, ELEMENT, 100, 1),
#     ]

def armor_loadout(pid: int, armor_type: str, quality):
    return [
        give(pid, f'{armor_type}_HELMET', 1, quality),
        give(pid, f'{armor_type}_SHIRT', 1, quality),
        give(pid, f'{armor_type}_PANTS', 1, quality),
        give(pid, f'{armor_type}_GLOVES', 1, quality),
        give(pid, f'{armor_type}_BOOTS', 1, quality),
    ]


def sniper_loadout(pid: int):
    quality = 0
    load = [
        #    f'ClearPlayerInventory {pid} 1 1 1',
    ]
    load += armor_loadout(pid, armor_type='GHILLIE', quality=quality)
    load += [
        give(pid, 'SNIPER_RIFLE', 1, quality),
        give(pid, 'ADVANCED_SNIPER_AMMO', 100, quality),
        give(pid, 'ADVANCED_SNIPER_AMMO', 100, quality),
    ]
    return load


def scrapper_loadout(pid: int):
    quality = 0
    load = [
        #    f'ClearPlayerInventory {pid} 1 1 1',
    ]
    load += armor_loadout(pid, armor_type='METAL', quality=quality)
    load += [
        give(pid, 'SWORD', 1, quality),
        give(pid, 'SHOTGUN', 1, quality),
        give(pid, 'LONGNECK_RIFLE', 1, quality),
        give(pid, 'SIMPLE_RIFLE_AMMO', 100, quality),
        give(pid, 'SIMPLE_SHOTGUN_AMMO', 100, quality),
    ]
    return load


def builder_loadout(pid: int):
    quality = 0
    load = []
    load += armor_loadout(pid, armor_type='HIDE', quality=quality)
    return [
        give(pid, 'METAL_HATCHET', 1, quality),
        give(pid, 'METAL_PICK', 1, quality),
        give(pid, 'METAL_SICKLE', 1, quality),
        give(pid, 'GPS', 1, quality),
    ]


def attacker_loadout(pid: int):
    quality = 10
    load = []
    load += armor_loadout(pid, armor_type='METAL', quality=quality)
    load += [
        give(pid, 'C4_DETONATOR', 1, 0),
        give(pid, 'C4', 10, 0),
    ]
    return load


def print_loadout_player(loadout_function, player_id):
    """ Print a player loadout function """
    for c in loadout_function(player_id):
        print(c)


def loadout_player(loadout_function, player_id):
    """ Load a player with a set of gear """
    for c in loadout_function(player_id):
        print(c)
        conn.exec_command(c)


def loadout_players(loadout_function, player_list):
    """ Load up a list of players with a set of gear """
    for player_id in player_list:
        loadout_player(loadout_function, player_id)


print("Establishing RCON connection")
conn = RconConnection('208.73.20.117', port=7870, password='abcthompson', single_packet_mode=True)

# conn.exec_command(join_tribe(THAD, "Tribe of Bo"))
# conn.exec_command("SpawnDino \"Blueprint'/Game/PrimalEarth/Dinos/Dodo/Dodo_Character_BP.Dodo_Character_BP'\" 82.7 37.7 1 1")

# loadout_player(scrapper_loadout, THAD)
# loadout_player(test_setup, BO)

# loadout_player(builder_loadout, THAD)
# loadout_player(builder_loadout, ZANE)

# loadout_player(builder_loadout, MALCOLM)
# loadout_player(scrapper_loadout, MALCOLM)

# loadout_player(test_loadout, MALCOLM)

# loadout_player(test_loadout, BO)

# loadout_players()
print_loadout_player(attacker_loadout, THAD)

print("DONE")
