import random

p1 = ["a","b","c","d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
p2 = ["a","b","c","d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def generate_name():
    part1 = random.choice(p1)

    part2 = random.choice(p2)
    if part1 == part2:
        while part1 == part2:
            part2 = random.choice(p2)

    part3 = random.choice(p1)
    if part3 == part2 or part3 == part1:
        while part3 == part2 or part3 == part1:
            part3 = random.choice(p1)
    
    part4 = random.choice(p2)
    if part4 == part3 or part4 == part2 or part4 == part1:
        while part4 == part3 or part4 == part2 or part4 == part1:
            part4 = random.choice(p2)


    name = part1 + part2 + part3 + part4 + part3 + part4
    return (name)

if __name__ == "__main__":
    for _ in range(100):
        print(generate_name())
