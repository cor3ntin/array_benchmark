import sys


print("""
int main() {
    int array[1+ 1204*1024*10] = { """);
for i in range(0, 1204*1024*10):
    sys.stdout.write("42, ")
print(""" 0};
}
""")