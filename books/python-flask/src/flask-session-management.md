# Session management

The HTTP protocol that is used for the web is stateless. Meaning that the server has no way of knowing if two request come from the same entity or not.

These days a browser my send several requets through the same connection, but that can be closed at any time. The browser will just establish a new connection and continue its request.

How can a server know that two request come from the same source? (the same browser, the same user etc.)?

The solution is the use of unique strings called cookies. When a server wants to establish an identity of the client it send a unique string. The browser then will send that unique string with every request it send to the server.

Based on these string the server can know if two requests come from the same source?
If they send the same unique value then they are from the same source.

In the next few pages we'll see how Flask helps us set and read cookies to manage sessions.

