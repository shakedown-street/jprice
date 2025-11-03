For a system to be scalable means that it can handle increased load, data, and users efficiently without a drop in performance or requiring a complete redesign.

There are two ways to scale a system:

### 1. Vertically (Scaling Up): Increase power to a single machine

**Pros**: Easier to implement and manage

**Cons**: Limited by the maximum capacity of a single machine and can lead to downtime during upgrades

> Example: Upgrading a backend server from 2 CPU cores/4GB RAM to 4 CPU cores/8GB RAM.

### 2. Horizontally (Scaling Out): Add more machines to distribute the load

**Pros**: Not limited by a single machine's capacity, better fault tolerance

**Cons**: More complex to implement and manage

> Example: Adding more backend servers to handle incoming requests.

---

To scale a web app horizontally, you can add more servers behind a **load balancer**.

Load balancing is the process of distributing incoming network traffic across multiple servers.

When a request comes to the system, it first passes through a load balancer, which decides which server will handle that request.

Here are some ways a load balancer can decide which server will handle the request:

1. **Round Robin**: Requests are distributed evenly across servers in a circular order.
2. **Least Connections**: Requests are sent to the server with the fewest active connections.
3. **IP Hash**: Requests are sent to a server based on the client's IP address.
4. **Weighted Round Robin**: Requests are distributed based on a server's weight (e.g. a server with a weight of 2 will receive twice as many requests as a server with a weight of 1).
5. **Least Response Time**: Requests are sent to the server with the lowest response time.

To scale a load balanced system, you can add more servers to the pool, or scale the existing servers vertically based on need.

---

## Scenario

- We will have two backend web servers running the application (such as a [Django](https://djangoproject.com/) backend)
- We will use [Nginx](https://nginx.org/) as a reverse proxy to distribute traffic between the two servers
- We will use Round Robin as the load balancing algorithm to distribute traffic evenly between the two servers

You will need to configure Nginx as a load balancer:

```nginx
http {
    upstream backend {
        # List of backend servers
        server 192.168.1.2;  # First server
        server 192.168.1.3;  # Second server
    }

    server {
        listen 80;  # Listen on HTTP port
        server_name your-domain.com;  # Use your domain name or IP

        location / {
            proxy_pass http://backend;  # Forward traffic to the 'backend' upstream block
            proxy_set_header Host $host;  # Pass host header
            proxy_set_header X-Real-IP $remote_addr;  # Real client IP
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  # Forwarded client IP
            proxy_set_header X-Forwarded-Proto $scheme;  # Protocol (HTTP or HTTPS)
        }
    }
}
```

Now, making a request to the nginx server's IP will distribute the traffic between the two backend servers using Round Robin.

#### Other configurations

1. IP Hash: Ensures that the same client IP always goes to the same server

```nginx
    upstream backend {
        ip_hash;  # Ensures that the same client IP always goes to the same server
        server 192.168.1.2;
        server 192.168.1.3;
    }
```

2. Load balancing based on server weight:

```nginx
    upstream backend {
        server 192.168.1.2 weight=3;  # Server gets more traffic
        server 192.168.1.3 weight=1;  # Server gets less traffic
    }
```

---

## Architecture

In the above scenario, both backend servers would be running the same code, and connecting to the same database server. Ideally the database should be hosted on a separate dedicated server so that it can be scaled independently from the backend servers as well. This could be an additional server or a service such as DigitalOcean's Managed Databases or RDS in AWS. Database servers can have their own scaling strategies such as read replicas, sharding, or vertical scaling which we won't get into here.

```less
       Client
          |
   [Load Balancer]
       /        \
  [Backend]  [Backend]
      |          |
    [Database Server]
```

---

One of the benefits of scaling out this way is that each server can be scaled independently. If you get more traffic to the web application, you can add more backend servers. If you need more database capacity, you can scale the database server. This allows you to scale the system as needed and optimize costs based on the specific needs of each component.

Backend servers should typically have similar specs to ensure that they can handle the same amount of traffic. If one server is more powerful than the other, it may become a bottleneck. A load balancer server can typically be more lightweight compared to the backend servers because it's just routing traffic and not processing the application logic. The database server will likely need to be the most powerful server in the stack.

---

## When to Use Load Balancing

When would load balancing not be necessary?

- Low traffic
- Minimize costs
- Simplicity is more important than scalability (small app or MVP) that you don't expect to grow much in the near future

When should you consider load balancing?

- You expect moderate traffic and want to future-proof
- You want to ensure better performance
- You want to ensure high availability and fault tolerance

---

## Summary

Load balancing is a powerful technique for scaling web applications horizontally. By distributing traffic across multiple backend servers, you can improve performance, ensure high availability, and handle increased load effectively. When designing a load balanced architecture, consider the specific needs of your application, including traffic patterns, resource requirements, and cost considerations.
