# AD Authentication

## NTLM Authentication

```mermaid
graph TD;

  A[Client Computer] -- Calculate NTLM Hash --> A[Client Computer] 
  
  A[Client Computer] -- Send Username --> B[App server]

  B[App server] -- Nonce/RandomValue --> A[Client Computer]

  A[Client Computer] -- Encrypted Nonce --> B[App Server] 

  B[App Server] -- Response/User/Nonce --> C[DC] -- using NTLM Hash --> D[Validation] -- Success --> C[DC] -- success --> E[Approve Authentication]

```

## Kerberos Authentication 

```mermaid
graph TD;

A[Client] -- Request --> B[DC] -- Validates --> C[Role] --> F[Success]


B[DC] -- Validates --> D[Authentication service request] --> F[Success]
B[DC] -- Validates --> E[hash containing username] --> F[Success]

B[DC] -- Decryption Success --> F[Success]
B[DC] -- Timestamp Not duplicate --> F[Success]

F[Success] -- Replies with Auth server reply with session key --> TGT --> A[client]

```

```mermaid
graph TD;

A[client] -- TGService Request --> B[DC]
B -- TGS validation -- TGServer Reply --> A[Client] 
```