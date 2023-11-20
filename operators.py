from algorithms.bubblesort import B
from algorithms.queuesort import Q
from algorithms.stacksort import S 
from algorithms.composition import compositionOf

BS = compositionOf(B,S)
BQ = compositionOf(B,Q)
QB = compositionOf(Q,B)
QS = compositionOf(Q,S)
SB = compositionOf(S,B)
SQ = compositionOf(S,Q)

# algorithmsIndex = {
# 	"B": B,
# 	"bubble" : B,
# 	"bubblesort" :B,
# 	"bubble-sort" :B,
# 	"S": S,
# 	"stack" : S,
# 	"stacksort" :S,
# 	"stack-sort" :S,
# 	"Q": Q,
# 	"queue" : Q,
# 	"queuesort" :Q,
# 	"queue-sort" :Q,
# 	"BS": BS,
# 	"bubble stack":BS,
# 	"BQ": BQ,
# 	"bubble queue": BQ 
# 	"QB": QB,
# 	"queue bubble": QB,
# 	"QS": QS,
# 	"queue stack": QS,
# 	"SB": SB,
# 	"stack bubble":SB,
# 	"SQ": SQ,
# 	"stack queue" SQ
# }