from collections import defaultdict, deque

def alien_order(words):
    # Step 1: Create graph and in-degree count
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}

    # Step 2: Build edges from adjacent words
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        # Edge case: prefix error (e.g. ["abc", "ab"])
        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
            return ""
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    in_degree[c2] += 1
                break

    # Step 3: Topological Sort (Kahn's Algorithm)
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    result = []

    while queue:
        char = queue.popleft()
        result.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If result doesn't contain all chars, there was a cycle
    if len(result) < len(in_degree):
        return ""

    return ''.join(result)

# === Hardcoded Input ===
words = ["wrt", "wrf", "er", "ett", "rftt"]

# === Run and Print Result ===
order = alien_order(words)
print("Alien Dictionary Order:", order)
