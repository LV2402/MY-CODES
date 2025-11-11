import heapq

def solve():
    vamshi_n = int(input().strip())
    vamshi_o = []
    for _ in range(vamshi_n):
        vamshi_a, vamshi_p, vamshi_v = map(int, input().split())
        vamshi_o.append((vamshi_a, vamshi_p, vamshi_v))
        
    vamshi_o.sort()
    
    vamshi_t = 0
    vamshi_i = 0
    vamshi_q = []
    vamshi_w = []
    
    while vamshi_i < vamshi_n or vamshi_q:
        if not vamshi_q and vamshi_i < vamshi_n:
            vamshi_t = max(vamshi_t, vamshi_o[vamshi_i][0])
        
        while vamshi_i < vamshi_n and vamshi_o[vamshi_i][0] <= vamshi_t:
            vamshi_a, vamshi_p, vamshi_v = vamshi_o[vamshi_i]
            heapq.heappush(vamshi_q, (-vamshi_v, vamshi_a, vamshi_p, vamshi_i))
            vamshi_i += 1
        
        if vamshi_q:
            vamshi_v, vamshi_a, vamshi_p, _ = heapq.heappop(vamshi_q)
            vamshi_s = max(vamshi_t, vamshi_a)
            if vamshi_s > vamshi_a:
                vamshi_w.append((vamshi_a, vamshi_s))
            vamshi_t = vamshi_s + vamshi_p
        else:
            vamshi_t = vamshi_o[vamshi_i][0]
    
    vamshi_e = []
    for vamshi_s, vamshi_e2 in vamshi_w:
        vamshi_e.append((vamshi_s, 1))
        vamshi_e.append((vamshi_e2, -1))
    vamshi_e.sort()
    
    vamshi_c = 0
    vamshi_ans = 0
    for _, vamshi_d in vamshi_e:
        vamshi_c += vamshi_d
        vamshi_ans = max(vamshi_ans, vamshi_c)
    
    print(vamshi_ans)

solve()
