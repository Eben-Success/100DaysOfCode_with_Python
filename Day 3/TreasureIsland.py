print('''

                           #####
                       #######
            ######    ########       #####
        ###########/#####\#####  #############
    ############/##########--#####################
  ####         ######################          #####
 ##          ####      ##########/@@              ###
#          ####        ,-.##/`.#\#####               ##
          ###         /  |$/  |,-. ####                 #
         ##           \_,'$\_,'|  \  ###
         #              \_$$$$$`._/   ##
                          $$$$$_/     ##
                          $$$$$        #
                          $$$$$
                         $$$$$
                         $$$$$
                         $$$$$        ___
                         $$$$$    _.-'   `-._
                        $$$$$   ,'           `.
                        $$$$$  /               \
~~~~~~~~~~~~~~~~~~~~~~~$$$$$~~~'~~~~~~~~~~~~~~~~`~~~~~~~~~~~~
   ~      ~  ~    ~  ~ $$$$$  ~   ~       ~          ~
       ~ ~      .o,    $$$$$     ~    ~  ~        ~
  ~            ~ ^   ~ $$$$$~        ______    ~        ~
_______________________$$$$$________|\\\\\\\_________________
                       $$$$$        |>\\\\\\\
    ______             $$$$$        |>>\\\\\\\
   \Q%=/\,\            $$$$$       /\>>|#####|
    `------`           $$$$$      /=|\>|#####|
                       $$$$$        ||\|#####|
                      $$$$$$$          ||"""||
                      $$$$$$$          ||   ||
                     $$$$$$$$$
"""""""""""""""""""""$$$$$$$$$""""""""""""""""""""""""""""""

''')
print("Welcome to Teasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at the crossroad, where do you want to go? Type "left" or "right".').lower()

if choice1 == 'left':
    # Continue the game
    input("You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swin" to swim across")

else:
    print("You fell into a hole. Game over")


