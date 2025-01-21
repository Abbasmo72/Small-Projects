## Net Sniffer
This code is a script for monitoring network traffic using the scapy library. It captures and logs network packets to a JSON file, helping in detecting unauthorized access by inspecting packet details.
<hr>

1. Importing Libraries:
   - <b>scapy.all:</b> For network-related functions like sniff (to capture packets), get_if_list (to get a list of network interfaces), and conf (for network configuration settings).
   - <b>datetime:</b> To get the current date and time.
   - <b>threading.Thread:</b> To run network monitoring in a separate thread (for concurrent execution).
   - <b>json:</b> To write packet details to a JSON file.
   - <b>time:</b> For measuring the execution time of the script.
