import time
import random

def test_tier_latency(tier_name, samples=100):
    """模拟不同记忆层级的检索延迟"""
    latencies = []
    
    # 模拟不同层级的延迟基准 (单位: ms)
    benchmarks = {
        "hot": (0.001, 0.005),   # <5ms
        "warm": (0.050, 0.150),  # 50-150ms
        "cold": (0.200, 0.500)   # 200-500ms
    }
    
    low, high = benchmarks.get(tier_name, (0.1, 0.5))
    
    print(f"Testing {tier_name} tier...")
    for _ in range(samples):
        # 模拟检索逻辑开销
        start = time.time()
        time.sleep(random.uniform(low, high)) 
        end = time.time()
        latencies.append((end - start) * 1000)
    
    avg = sum(latencies) / samples
    p95 = sorted(latencies)[int(samples * 0.95)]
    print(f"Results: Avg={avg:.2f}ms, P95={p95:.2f}ms")
    return avg, p95

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--tiers", default="hot,warm,cold")
    parser.add_argument("--samples", type=int, default=100)
    args = parser.parse_args()
    
    tiers = args.tiers.split(",")
    print("-" * 30)
    print(f"{'Tier':<10} | {'Avg Latency':<12} | {'P95 Latency'}")
    print("-" * 30)
    for t in tiers:
        avg, p95 = test_tier_latency(t.strip(), args.samples)
        print(f"{t.strip():<10} | {avg:>10.2f}ms | {p95:>10.2f}ms")
