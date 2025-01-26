import os
import pkg_resources

def calc_container(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

dists = list(pkg_resources.working_set)
dist_sizes = []

for dist in dists:
    try:
        path = os.path.join(dist.location, dist.project_name)
        size = calc_container(path)
        dist_sizes.append((dist, size))
    except OSError:
        print(f'{dist.project_name} no longer exists')

# Sort by size
dist_sizes.sort(key=lambda x: x[1], reverse=True)

# Print sorted sizes
for dist, size in dist_sizes:
    if size / 1000 > 1.0:
        print(f"{dist}:, {size / 1000} KB")