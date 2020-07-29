from pypokerengine.api.game import setup_config, start_poker
from fishplayer import FishPlayer
from consoleplayer import ConsolePlayer
from randomplayer import RandomPlayer
from honestplayer import HonestPlayer
'''
The random player, well, performs random decisions.
The fish player always calls.
The console player let you participate using the console.
10 players in total
'''
config = setup_config(max_round=2, initial_stack=10000, small_blind_amount=20)
config.register_player(name="Fish1", algorithm=FishPlayer())
config.register_player(name="Fish2", algorithm=FishPlayer())
config.register_player(name="Fish3", algorithm=FishPlayer())
config.register_player(name="Fish4", algorithm=FishPlayer())
config.register_player(name="Random1", algorithm=RandomPlayer())
config.register_player(name="Random2", algorithm=RandomPlayer())
config.register_player(name="Random3", algorithm=RandomPlayer())
config.register_player(name="Random4", algorithm=RandomPlayer())
config.register_player(name="Random5", algorithm=RandomPlayer())
#config.register_player(name="h1", algorithm=HonestPlayer())
config.register_player(name="DrDram", algorithm=ConsolePlayer())
game_result = start_poker(config, verbose=1)
