'''Problem: Asteroid Collision
You’re given a list of integers representing asteroids moving along a line.
Positive values → asteroids moving right
Negative values → asteroids moving left
Asteroids move at the same speed.

When two asteroids moving in opposite directions meet:
The smaller one explodes
If they are equal, both explode
If they move in the same direction, nothing happens
Your goal: Return the state of the asteroids after all collisions.

✅ Key Rule:
Only a left-moving asteroid (-ve) that comes after a right-moving asteroid (+ve) can cause a collision.

💡 Idea: Use a Stack
We use a stack to keep track of asteroids:
Push all positive asteroids (they're moving right)
When a negative asteroid appears:
Keep checking the top of the stack
While there's a smaller positive asteroid on top → pop it (it explodes)
If both are equal → pop the top and don't push the negative (both explode)
If the negative is smaller → it explodes (do nothing)
If there's no positive asteroid to fight → just push the negative one
'''
stk = []
for ast in asteroids:
    if ast > 0:
        # Asteroid moving right — just push to stack
        stk.append(ast)
    else:
        # Asteroid moving left — possible collision
        while stk and stk[-1] > 0 and stk[-1] < abs(ast):
            # Stack top is smaller positive → it explodes
            stk.pop()
        if stk and stk[-1] == abs(ast):
            # Both are equal → both explode
            stk.pop()
        elif not stk or stk[-1] < 0:
            # No collision → push the negative asteroid
            stk.append(ast)
return stk
