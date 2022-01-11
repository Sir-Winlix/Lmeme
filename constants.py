PROCESS_NAME = 'League of Legends.exe'

oObjectManager = 0x186EE44
oObjectMapRoot = 0x28
oObjectMapNodeNetId = 0x10
oObjectMapNodeObject = 0x14

OBJECT_SIZE = 0x33C0
oObjectAbilityPower = 0x1788
oObjectArmor = 0x12E4
oObjectArmorBonus = 0x12F0
oObjectAtkRange = 0x1304
oObjectAtkSpeedMulti = 0x12B8
oObjectBaseAtk = 0x12BC
oObjectBonusAtk = 0x1234
oObjectHealth = 0xDB4
oObjectMaxHealth = oObjectHealth + 0x10
oObjectInvulnerable = 0x3EC
oObjectLevel = 0x339C 
oObjectMagicRes = 0x12EC 
oObjectMagicResBonus = 0x12F0
oObjectMana = 0x2B4
oObjectMissileIndex = 0x6C
oObjectMissileSpellCast = 0x250
oObjectPos = 0x1F4
oObjectTeam = 0x4C
oObjectTargetable = 0xD1C
oObjectVisibility = 0x28C
oObjectName = 0x2BE4
oObjectNetworkID = 0xCC
oObjectRecalling = 0xDA8
oObjectSizeMultiplier = 0x12D4
oObjectSpawnCount = 0x2A0
oObjectSpellBook = 0x2370
oObjectSpellBookArray = 0x488
oObjectBuffManager = 0x21B8
oObjectBuffManagerEntriesStart = oObjectBuffManager + 0x10
oObjectBuffManagerEntriesEnd = oObjectBuffManager + 0x14

SPELL_SIZE = 0x30
oSpellSlotLevel = 0x20
oSpellSlotCooldownExpire = 0x28

BUFF_SIZE = 0x78
oBuffInfo = 0x8
oBuffCount = 0x74
oBuffEndTime = 0x10
oBuffInfoName = 0x8

oObjectX = oObjectPos
oObjectZ = oObjectPos + 0x4
oObjectY = oObjectPos + 0x8

oZoomClass = 0x3103410
oLocalPlayer = 0x310B984
oViewProjMatrices = 0x3134E68
oRenderer = 0x310B9A0
oRendererWidth = 0x0
oRendererHeight = 0x4
oGameTime = 0x31034D4
