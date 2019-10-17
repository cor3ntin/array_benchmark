import sys


print("""
int main() {
    auto string = "\\""");
for i in range(0, 1204*1024*10):
    sys.stdout.write("\\x42")
print("""";
}
""")