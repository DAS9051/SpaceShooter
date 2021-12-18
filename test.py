import time

def heat_bar(heat):

    percent_done = (heat+1)/100*100
    percent_done = round(percent_done, 1)

    done = round(percent_done/(100/50))
    togo = 50-done

    done_str = '🟥'*int(done)
    togo_str = '⬜'*int(togo)

    print(f'Heat: [{done_str}{togo_str}] {percent_done}% heated')




r = 100
for i in range(r):
    heat_bar(i)
    time.sleep(.02)