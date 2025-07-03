# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eclipse-zenoh==1.4.0",
# ]
# ///
import zenoh

key = "**"
zenoh.init_log_from_env_or("error")
print("Opening session...")
with zenoh.open(zenoh.Config.from_file("/zenoh_client_config.json5")) as session:
    print(f"Declaring Subscriber on '{key}'...")
    with session.declare_subscriber(key) as sub:
        print("Press CTRL-C to quit...")
        for sample in sub:
            print(f"sub got {sample.key_expr}  {sample.payload.to_string()}")
