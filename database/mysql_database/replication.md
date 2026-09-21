### **What is Replication in MySQL?**
```sql

Replication is the process of copying data from one MySQL server to one or more other MySQL servers automatically.

        Primary (Master)
              |
     -------------------
     |                 |
 Replica 1        Replica 2
 (Slave)          (Slave)

When data changes on the Primary (Source/Master) server, those changes are copied to the Replica (Replica/Slave) servers.

Why Use Replication?
1. Read Scalability

Without replication:

Application
     |
     V
 Single Database

All read and write requests go to one server.

With replication:

          Primary
             |
      ----------------
      |              |
   Replica1      Replica2
Writes → Primary
Reads → Replicas

This reduces load on the primary server.

2. High Availability

If primary fails:

Primary ❌

A replica can be promoted as the new primary.

3. Backup Reporting

Run heavy reports on replicas instead of the production server.

How Replication Works

Suppose:

INSERT INTO employees
VALUES (1,'Mohit',50000);
Step 1

Write happens on Primary.

Step 2

MySQL records the change in the Binary Log (Binlog).

Primary
   |
 Binary Log
Step 3

Replica reads the binlog.

Step 4

Replica applies the same change.

Primary
   |
 Binlog
   |
 Replica

Now both servers have the same data.

Types of Replication
1. Asynchronous Replication

Most common.

Client
  |
Primary -----> Replica
      (later)
Flow
Primary commits transaction.
Client gets success response.
Replica receives changes later.
Advantage

Fast.

Disadvantage

Replica may lag behind.

2. Semi-Synchronous Replication
Primary
   |
Waits for at least one Replica ACK

Transaction is considered complete only after at least one replica acknowledges receiving it.

Advantage

Less chance of data loss.

Disadvantage

Slightly slower.

3. Group Replication

Multiple MySQL servers work together as a cluster.

Server A
Server B
Server C

Used for high availability and fault tolerance.

Replication Terminology
Old Term	New Term
Master	Source
Slave	Replica

Modern MySQL documentation uses Source and Replica.

Replication Lag

Sometimes replica is behind primary.

Example:

Primary → 1000 records
Replica → 995 records

5 records are not yet copied.

This delay is called Replication Lag.

Check:

SHOW REPLICA STATUS\G

Look for:

Seconds_Behind_Source
Replication vs Backup
Replication	Backup
Continuous data copy	Snapshot of data
Near real-time	Point-in-time
High availability	Disaster recovery
Not a backup replacement	Required separately

Interview Point:

Replication is not a backup strategy. If data is accidentally deleted on the primary, that deletion is also replicated to replicas.

Replication vs Clustering
Replication	Clustering
One primary, multiple replicas	Multiple active nodes
Mainly for read scaling	High availability + scaling
Simpler	More complex
Common Interview Questions
Q1. Can Replica Accept Writes?

Normally:

No

Replica is read-only.

Writes go to the primary.

Q2. What is Binlog?

A file containing all database changes.

Replication uses binlogs to copy data.

Q3. What happens if Primary crashes?

A replica can be promoted to become the new primary.

This process is called Failover.

Interview Answer (Short)

Replication is a feature in MySQL that copies data from a primary (source) server to one or more replica servers. It is used for read scalability, high availability, failover, and reporting. MySQL replication works through binary logs (binlogs), where changes made on the primary are recorded and replayed on replicas. Common types include asynchronous, semi-synchronous, and group replication.
```