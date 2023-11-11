def isValidChessBoard(dict):
    bking = 0
    wking = 0
    w_pieces = 0
    b_pieces = 0
    l_pos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    l_nos = ['1', '2', '3', '4', '5', '6', '7', '8']
    l_pieces = ['wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen','wking', 'bpawn', 'bknight', 'bbishop', 'brook', 'bqueen','bking']
    
    
    for j in dict.keys():
        if j[0] not in l_nos:
            return False     
        if j[1] not in l_pos:
            return False    
        
    
    for i in dict.values():
        if i not in l_pieces:
            return False
        if i[0] == 'w':
            w_pieces += 1
        if i[0] == 'b':
            b_pieces += 1
        if i[0] == 'wking':
            wking += 1
        if i[0] == 'bking':
            bking += 1         
        
        if bking > 1 or wking > 1 or w_pieces>16 or b_pieces>16:
            return False 
            
    return True            
            
              

moves = {'1h': 'bking', 
         '6c': 'wqueen', 
         '2g': 'bbishop', 
         '5h': 'bqueen', 
         '3e': 'wking'} 
   
print(isValidChessBoard(moves))    