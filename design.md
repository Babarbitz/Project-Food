Game Controller:

    + gameloopControl           : bool
    - playerController          : PlayerController
    - inventroyController       : InventoryController
    - inputController           : InputController
    - menuController            : MainMenuController
    - mapController             : MapController
    - shopController            : ShopController
    - enemyController           : EnemyController

    -----------------------------------------------

    + handleEvents()
    + saveGame
    + loadGame
    + newGame

-------------------------------------------------
Main Menu UI:

    - sprites           : Spritelist
    - positions         : List <(int,int)>
    - text              : List <pygame.text>

    ---------------------------------------

    + updateUI()

Main Menu Controller:

    - currentSelection    : int
    - options             : List <text>
    - saveData            : SaveData
    - menuUI              : MainMenuUI

    ---------------------------------

    + updateUI()
    + loadSaveData()

Save Data:

    - map           : digraph <Room>
    - inventory     : Inventory
    - player        : Player

    ---------------------------------

    + getInventory()    : Inventory
    + getMap()          : Map
    + getPlayer()       : Player

--------------------------------------------------

Input Controller:

    - exitSignal        : bool
    - mode              : Mode
    - inputs            : List <InputType>

    ----------------------------

    + handleEvents
    + getInputs()                   : List <InputType>
    + getExitSignal()               : bool
    - addInput(i : InputType)
    - removeInput(i : InputType)
    - keyPress(e : pygame.event)
    - keyRelease(e : pygame.event)
    - setExitSignal(val : bool)

--------------------------------------------------

Menu UI:

    - sprites           : Spritelist
    - positions         : List <(int,int)>
    - text              : List <pygame.text>

    ---------------------------------------

    + updateUI()

--------------------------------------------------

Player:

    - attack Cooldown Frame : int
    - currentHP             : int
    - currentSprite         : Sprite
    - damage                : int
    - id                    : ID
    - maxHP                 : int
    - position              : (int,int)
    - states                : List <state>

    ---------------------------------------

    + getAttackCooldownFrame()  : int
    + getCurrentHP()            : int
    + getCurrentSprite()        : Sprite
    + getDamage()               : int
    + getId()                   : ID
    + getMaxHP()                : int
    + getPosition()             : (int,int)
    + getStates()               : state

    + setAttackCooldownFrame(frame : int)
    + setCurrentHP(hp : int)
    + setCurrentSprite(sprite : Sprite)
    + setDamage(damage : int)
    + setId(id : ID)
    + setMaxHP(hp : int)
    + setPosition(pos : (int,int))
    + setStates(List <States>)

Player Controller:

    - player            : Player
    - sprites           : Spritelist
    - renderable        : bool
    - updatable         : bool
    - collidable        : bool
    - frameCounter      : int
    - UI                : PlayerUI

    --------------------------------

    + AttackNorth()
    + AttackSouth()
    + AttackEast()
    + AttackWest()
    + MoveNorth()
    + MoveSouth()
    + MoveEast()
    + MoveWest()
    + save()
    + update()
    - Attack()
    - Move
    - updateUI()
    - updateStates()
    - checkCollision()
    - collideWall()
    - collideEnemy()
    - takeDamage()

Player UI:

    - sprites           : Spritelist
    - positions         : List <(int,int)>
    - text              : List <pygame.text>

    ---------------------------------------

    + updateUI()

--------------------------------------------------

Inventory:

    supplies    : List <Supply>
    items       : List <Item>

    ------------------------------------

    + getCraftingSupplies()                     : List <Supply>
    + getItems()                                : List <Item>
    + setCraftingSupplies(supplies : List <Supply>)
    + setItems(items : List <Item>)

Inventory UI:

    - sprites           : Spritelist
    - positions         : List <(int,int)>
    - text              : List <pygame.text>

    ---------------------------------------

    + setPositions()
    + updateUI()

Crafting UI:

    - sprites           : Spritelist
    - positions         : List <(int,int)>
    - text              : List <pygame.text>

    ---------------------------------------

    + setPositions()
    + updateUI()
￼
Inventory Controller:

    - selectedItem      : int
    - showInventory     : bool
    - inventory         : Inventory
    - inventoryUI       : InventoryUI
    - craftingUI        : CraftingUI
    --------------------------

    + craftReciepe()
    + updateUI()
    + addItem(i : item)
    + removeItem(i : item)
    + useItem()

--------------------------------------------------

Room:

    - backGround            : Sprite
    - walls                 : List <Wall>
    - structures            : List <Structure>
    - doors                 : List <Door>
    - enemies               : List <Enemy>

    -------------------------------------------

    + checkDoors()
    + render()

Map Controller:

    - Level         : digraph <Room>
    - currentLevel  : int

    ---------------------------------

    + generateLevel()
    + loadLevel()
    + changeRoom()

--------------------------------------------------

Shop UI:

    - sprites           : Spritelist
    - positions         : List <(int,int)>
    - text              : List <pygame.text>

    ---------------------------------------

    + updateUI()

Shop Controller:

    - inventory         : Inventory
    - shopUI            : ShopUI
    - isOpen            : bool

    --------------------------------

    + updateShop()
    - updateInventory()
    - close()

--------------------------------------------------

Enemy:

    - attack Cooldown Frame : int
    - currentHP             : int
    - currentSprite         : Sprite
    - damage                : int
    - id                    : ID
    - maxHP                 : int
    - position              : (int,int)
    - states                : List <state>

    ---------------------------------------

    + getAttackCooldownFrame()  : int
    + getCurrentHP()            : int
    + getCurrentSprite()        : Sprite
    + getDamage()               : int
    + getId()                   : ID
    + getMaxHP()                : int
    + getPosition()             : (int,int)
    + getStates()               : state

    + setAttackCooldownFrame(frame : int)
    + setCurrentHP(hp : int)
    + setCurrentSprite(sprite : Sprite)
    + setDamage(damage : int)
    + setId(id : ID)
    + setMaxHP(hp : int)
    + setPosition(pos : (int,int))
    + setStates(List <States>)

    + move(playerPos : (int,int))
    + kill()

Enemy Controller:

    - enemies           : List <Enemy>
    - playerPosition    : (int,int)

    -----------------------------------

    + updateEnemies()
    - argoEnemy()
    - idleEnemy()
    - killEnemy(e : Enemy)
    - placeEnemy(e : Enemy)


