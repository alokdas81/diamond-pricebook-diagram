### **LCN [CAN113462_LCN_Price_Book_13_Feb2023_RevJun2023_07-05-23](./CAN113462_LCN_Price_Book_13_Feb2023_RevJun2023_07-05-23.pdf):**

**Finish Codes:**
![Finish chart Image](../finish_codes.png)
```mermaid
flowchart TD


subgraph Series Selection
A[Possible Options]
B[1250] 
C[1260T]
D[4000T]
E[2010]
F[3130SE]
G[etc.]
end

A --> B
A --> C
A --> D
A --> E
A --> F
A --> G

```
- **Product dependent Required Params:**

```mermaid
graph TB

subgraph Handing selection
S[Possible Options]
S --> RH[Right Hand]
S --> LH[Leftt Hand]
end

subgraph Device Finish Selection
Q[Possible Options]
Q --> |BHMA Number| 616
Q --> |BHMA Number| 652
Q --> |BHMA Number| 691
Q --> |BHMA Number| 690
Q --> |BHMA Number| 622
Q --> |BHMA Number| 689
Q --> R[etc.]
end


subgraph Arm type Selection
G[Possible Options]
H[REGARM]
I[RWPA]
J[LONG]
K[etc.]
end


subgraph Model Selection
A[Possible Options]
B[1250]
C[1261]
D[4003T]
E[4011]
F[etc.]
end

A --> |1250| B
A --> |1260| C
A --> |4000T| D
A --> |4010| E
A --> F

G --> H
G --> I
G --> J
G --> K

```
- **Base price chart:**

![1250 Series Base price Image](./images/base_price_list.png)
- **Optional Params:**

```mermaid
graph TB


subgraph Track selection
N[Possible Options] --> O[BUMP: Track with Bumper]
N --> P[H: Hold Open Track]
N --> Q[HBMP: Hold Open Track with Bumper]
N --> R[LONG: Long Track]
N --> S[STDSECTRK: Standard Security Track]
N --> T[STDTRK: Standard Track]
N --> U[etc.]
end

subgraph Cover selection
A[Possible Options] --> B[STD: Standard cover]
A --> C[DEL: Delay action cylinder]
A --> D[DPS: DPS cylinder]
A --> E[LESS: Less cover]
A --> F[etc.]
end

subgraph Cylinder selection
G[Possible Options] --> H[STD: Standard cylinder]
G --> I[SLIMPC: Slim Plastic cover]
G --> J[FPC: Full plastic cover]
G --> K[MC: Metal cover]
G --> L[LESSCOV: Less cylinder]
G --> M[etc.]
end

```

```mermaid
flowchart TD

subgraph Closer stop Type selection
N[Possible Options] --> O[No Stop]
N --> P[Positive stop]
N --> Q[Breakaway stop]
end

subgraph Voltage selection
G[Possible Options] --> H[12V]
G --> I[24V]
G --> J[115V]
G --> K[120V]
G --> L[240V]
G --> M[etc.]
end

subgraph Screw Package selection
A[Possible Options] --> B[WMS: Wood & Machine screws]
A --> C[Torx: TORX Machine screws]
A --> D[SPEC: Special screw package]
A --> E[LESS: Less Screw package]
A --> F[etc.]
end

```

```mermaid
flowchart TD


subgraph Header Bracket selection
A[Possible Options] --> B[Angle Brackets]
A --> C[Dress plates]
end

subgraph Header Length selection
Q[Possible Options] --> R[33]
Q --> S[33-1/8]
Q --> T[33-1/4]
Q --> U[33-3/8]
Q --> V[33-1/2]
Q --> W[33-5/8]
Q --> X[33-3/4]
Q --> Y[33-7/8]
Q --> Z[34]
Q --> ZZ[etc.]
end

subgraph Header Type selection
N[Possible Options] --> O[HDR: Single door]
N --> P[HDR2: Double door]
end
```

```mermaid
flowchart TD


subgraph Controller selection
A[Possible Options] --> B[CTRL: Standard Controller]
A --> C[CTRL2: Standard Controller, pair]
end

subgraph Spindle center selection
Q[Possible Options] --> R[2-3/4]
Q --> S[3-3/4]
Q --> T[12-1/4]
end

subgraph Gearbox selection
N[Possible Options] --> O[MGB: Standard Motor Gearbox]
N --> P[MGB2: Standard Motor Gearbox, Pair]
end
```

```mermaid
flowchart TD

G[SRI Primer]
H[Buy america act]
I[Flush ceiling application]
J[Concealed switch]
P[Possible Options]
G --> P 
H --> P 
I --> P 
J --> P 
P --> Y[yes] 
P --> N[No] 

```
- **Optional price chart:**

![1250 Series Options Image](./images/adon_price_list.png)
![2810 Series Options Image](./images/adon_price_list2.png)
![9530 Series Options Image](./images/adon_price_list3.png)
