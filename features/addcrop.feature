Feature: track the state of the crops
    As thg system administor
    I want farmers to be able to track state of crops
    so that farmers can know the state of the crops
    
    Scenario Outline: Add crop to farms
    Given at the crop screen
    When a farmer submit the <id> <cropname>, <growstate> and <farmid>
    Then the system should return "You success added crop"
    Examples:
        |id|cropname|growstate|farm_id|
        |1|corn|plant|1|
        |2|banana|plant|2|
        |3|wheat|plant|3|
        |4|redbull|harvest|4|
       
        
    Scenario Outline: remove crop from farms
    Given at the crop screen
    When a farmer submit the <cropname>, <growstate> and <farmid>
    Then the system should return "successfully removed"
    Examples:
        |cropname|growstate|farm_id|
        |corn|plant|1|
        |banana|plant|2|
        |wheat|plant|3|
        |redbull|harvest|4|
        
    Scenario Outline: add crop to not empty farm
    Given at the crop screen
    When a farmer submit the <cropname>, <growstate> and <farmid>
    Then the system should return "sorry, this farm has no place for more crops"
    Examples:
        |cropname|growstate|farm_id|
        |corn|plant|1|
        |banana|plant|2|
        |wheat|plant|3|
        |redbull|harvest|4|
        
    Scenario Outline: show the state of crops
    Given at the crop screen
    When a farmer choose one farm
    Then the system should return growing states of all crops
    
    