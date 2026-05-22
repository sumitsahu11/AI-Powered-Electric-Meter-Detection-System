import glob
import os

root = r"C:\Users\Victus\meter_detection_project\data\dataset\labels"

# Show classes before fixing
print("Before fixing:")
for split in ["train", "val", "test"]:
    d = os.path.join(root, split)
    classes = set()
    if not os.path.isdir(d):
        print(split, "-> no dir")
        continue
    for f in glob.glob(os.path.join(d, "*.txt")):
        with open(f) as fh:
            for line in fh:
                if not line.strip():
                    continue
                try:
                    cid = int(line.split()[0])
                except Exception:
                    continue
                classes.add(cid)
    print(split, "classes:", sorted(classes))

# Force all class ids to 0
for split in ["train", "val", "test"]:
    d = os.path.join(root, split)
    if not os.path.isdir(d):
        continue
    for f in glob.glob(os.path.join(d, "*.txt")):
        lines = []
        with open(f) as fh:
            for line in fh:
                if not line.strip():
                    continue
                parts = line.split()
                parts[0] = "0"
                lines.append(" ".join(parts))
        with open(f, "w") as fh:
            fh.write("\n".join(lines) + "\n")

# Show classes after fixing
print("\nAfter fixing:")
for split in ["train", "val", "test"]:
    d = os.path.join(root, split)
    classes = set()
    if not os.path.isdir(d):
        print(split, "-> no dir")
        continue
    for f in glob.glob(os.path.join(d, "*.txt")):
        with open(f) as fh:
            for line in fh:
                if not line.strip():
                    continue
                try:
                    cid = int(line.split()[0])
                except Exception:
                    continue
                classes.add(cid)
    print(split, "classes:", sorted(classes))
