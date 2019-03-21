Game Controller:



--------------------------------------------------

Player:

    - sprites           : Spritelist
    - currentSprite     : Sprite
    - rectangle         : rectangle
    - renderable        : bool
    - updatable         : bool
    - collidable        : bool
    - frame             : int
    - id                : ID
    - states            : state

    - max HP                : int
    - current HP            : int
    - damage                : int
    - attack Cooldown Frame : int
    --------------------------------
    + AttackNorth()
    + AttackSouth()
    + AttackEast()
    + AttackWest()
    + MoveNorth()
    + MoveSouth()
    + MoveEast()
    + AttackWest()
    + getPosition() : (int,int)
    + update()
    - checkStates()
    - checkCollision()
    - collideWall()
    - collideEnemy()
    - takeDamage()

--------------------------------------------------

Input: - DONE

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
