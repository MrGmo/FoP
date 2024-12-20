**Lesson 2**

# How The Internet Works

The Internet enables computers worldwide to exchange data using a standardized set of rules called protocols. It relies on physical infrastructure (cables, routers, data centers) and abstract protocols (like HTTP, TCP/IP) to function seamlessly.

In short, the Internet is essensially just a bunch of connected computers that communicate between each other.

## Key Concepts

* **Network**: A group of interconnected computers
* **IP Address**: A unique identifier for a device on the internet. Think of an address to a home.
* **Packets**: Small chuncks of data sent across the internet. Broken down data that disassembles and reassembles at its destination.
* **Protocol**: A set of rules for how devices communicate (HTTP, HTTPS, FTP).
* **Router**: A device that directs packets to their destination

## How Data Travels

1. **Data Conversion**: Data (Like an email) is broken into smaller units.
2. **Transmission**: Packets are sent from the source computer to the destination using routers.
3. **Routing**: Routers analyze each packet and determine the fastest path to the destination
4. **Reassmembly**: Packets are reassembled at the destination to form the original data.

## Core Internet Protocols

The internet works using several key protocols.

* **IP (Internet Protocol)**: Responsible for addressing and routing packets.
* **TCP (Transmission Control Protocol)**: Ensures reliable delviery of packets.
* **HTTP/HTTPS (Hyptertest Transfer Protocol)**: Enables the transfer of web pages.
* **DNS (Domain Name System)**: Translates human-readable domain names into IP addresses.

## Domain Name System (DNS)

The DNS is like the internet's phonebook. When you type a website's name (`www.example.com`) into your browser:

1. The browser queries a DNS server to find the website's IP address.
2. The DNS server returns the IP address (`192.168.1.1`).
3. The browser uses this IP address to connect to the server hosting the website

## Client - Server Model

The internet operates on a client-server model:
* **Client**: Your device (computer, smartphone) that requests data.
* **Server**: A powerful computer that stores data and sends it to clients

For example:
1. You type `www.example.com` into your browser.
2. Your browser (client) sends a request to the server hosting the website.
3. The server processes the request and sends back the data (HTML, CSS, JavaScript).

## Key Components of the Internet

1. **Physical Layer**: Includes cables, fiber optics, and satellites.
2. **ISP (Internet Service Provider)**: Provides access to the Internet.
3. **Routers and Switches**: Direct packets to their destinations.
4. **Servers**: Host websites, applications, and other online content.

## Conclusion

HTML is the cornerstone of web development, enabling developers to create structured and accessible content for the web. By mastering HTML, you can build robust and visually appealing websites.

##

Once VS Code is installed on your machine click on the extensions button on the left hand menu. Next, search and install the following extensions: Live Server, Prettier, Quokka, Rainbow CSV, and VS Code Icons. These extensions will come in handy later in the course.

Class Work:

1. Complete the brownies.html file with the semantically appropriate tags.

2. Build a bbc.html file with all the appropriate tags so that it mirrors the BBC.png picture that is included in this folder.

Extra Resources on HTML/CSS:

1. https://learn.shayhowe.com/html-css/
2. https://developer.mozilla.org/en-US/docs/Web/HTML
