import functions

def main():
    """
    game = {
        "player_1":"Péter",
        "player_2":"Mari",
        "num_of_rounds": 3,
        "rounds": {
            1:{
                "choice_player_1":"paper",
                "choice_player_2":"rock",
                "winner":"player_1"
            },
            2:{
                "choice_player_1":"paper",
                "choice_player_2":"rock",
                "winner":"player_1"
            },
            3:{
                "choice_player_1":"paper",
                "choice_player_2":"rock",
                "winner":"player_1"
            }
        },
        "player_1_pts": 2,
        "player_2_pts": 1,
        "result" : "Péter (2:1)"
    }
    """

    functions.clear_console()
    game = functions.get_names_n_round()
    functions.show_teaser(game)
    functions.play(game)
    functions.show_result(game)    

main()