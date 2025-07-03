# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eclipse-zenoh==1.4.0",
# ]
# ///
import time

import zenoh

key = "**"
zenoh.init_log_from_env_or("error")
print("Opening session...")
with zenoh.open(zenoh.Config.from_file("/zenoh_client_config.json5")) as session:
    pubs: list[zenoh.Publisher] = []
    for i in range(600):
        pubs.append(session.declare_publisher(key_expr=f"pub/{i}"))
    
    start = time.perf_counter_ns()
    for pub in pubs:
        pub.put(f"hello from {pub.key_expr}")
    end = time.perf_counter_ns()
    print(f"first pub took: {(end-start)/1e9} s")
    
    start = time.perf_counter_ns()
    for pub in pubs:
        pub.put(f"hello 2 from {pub.key_expr}")
    end = time.perf_counter_ns()
    print(f"second pub took: {(end-start)/1e9} s")

    start = time.perf_counter_ns()
    for pub in pubs:
        pub.put(f"hello 3 from {pub.key_expr}")
    end = time.perf_counter_ns()
    print(f"third pub took: {(end-start)/1e9} s")
