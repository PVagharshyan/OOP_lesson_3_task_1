import vertex
import random

count = 5
list_verts = []

def main() -> None:
    for i in range(count):
        x = random.randint(vertex.vertex.min(), vertex.vertex.max())
        y = random.randint(vertex.vertex.min(), vertex.vertex.max())
        list_verts.append(vertex.vertex(x, y))

    for item in list_verts:
        print(item)

if __name__ == "__main__":
    main()
