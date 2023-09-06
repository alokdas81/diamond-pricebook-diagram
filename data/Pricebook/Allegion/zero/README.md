### **Zero [CAN110962_Zero_Price_Book_10_Feb2023_RevJun2023_07-05-23](./CAN110962_Zero_Price_Book_10_Feb2023_RevJun2023_07-05-23.pdf):**

**Finish Codes:**
![Finish chart Image](./images/finish_chart.png)
```mermaid
flowchart TD


subgraph Series Selection
A[Possible Options]
B[15] 
C[63]
D[622]
E[360]
F[361]
J[7350]
G[etc.]
H[Thresholds]
I[Autometic door bottoms]
end

A --> B --> |Product Category| H
A --> C --> |Product Category| H
A --> D --> |Product Category| H
A --> E --> |Product Category| I
A --> F --> |Product Category| I
A --> J --> |Product Category| I
A --> G

```
**1. Thresholds [15 series, 63 Series, 622 Series etc.]:**
- **Product dependent Required Params:**

```mermaid
flowchart TD

subgraph Finish selection
A[Possible Options]
A --> |Desc/Code/BHMA| B[Aluminum/A/-]
A --> |Desc/Code/BHMA| C[Aluminum clear anodized/AA/628]
A --> |Desc/Code/BHMA| D[Bronze/B/-]
A --> |Desc/Code/BHMA| E[Aluminum black anodized/BK/711]
A --> |Desc/Code/BHMA| F[High buff polished bronze/B-POL/-]
A --> |Desc/Code/BHMA| G[Oil-rubbed bronze/B-ORB/613]
A --> H[etc.]
end
```
```mermaid
flowchart TD

subgraph Length selection
Q[Possible Options]
Q --> J[6]
Q --> S[6-1/8]
Q --> T[6-1/4]
Q --> U[6-3/8]
Q --> V[6-1/2]
Q --> W[6-5/8]
Q --> X[6-3/4]
Q --> Y[6-7/8]
Q --> Z[7]
Q --> ZZ[etc.]
end

```
- **Base price chart:**

![63 Series Base price Image](./images/base_price_list.png)

- **Product dependant Optional Params:**

```mermaid
flowchart TD

A[Full Body Strength/V3]
B[No Hole/NH]
P[Possible Options]
A --> P 
B --> P 
G[etc.] 
P --> Y[yes] 
P --> N[No] 
```
```mermaid
graph TB


subgraph Epoxy selection
A[Possible Options] --> B[E: Epoxy tread]
A --> C[EL: Photoluminescent and epoxy tread]
end

subgraph Expansion shield/Anchors selection
Q[Possible Options] --> 221
Q --> 222
Q --> 223
Q --> 224
Q --> 226
end

```
- **Optional price chart:**

![Adon charges Image](./images/adon_charges.png)
![Adon part charges Image](./images/adon_part_price.png)

**2. Autometic door bottoms [360 series, 361 Series, 7350 Series etc.]:**
- **Product dependent Required Params:**

```mermaid
flowchart TD

subgraph Finish selection
A[Possible Options]
A --> |Desc/Code/BHMA| B[Aluminum/A/-]
A --> |Desc/Code/BHMA| C[Aluminum clear anodized/AA/628]
A --> |Desc/Code/BHMA| D[Bronze/B/-]
A --> |Desc/Code/BHMA| E[Aluminum black anodized/BK/711]
A --> |Desc/Code/BHMA| F[High buff polished bronze/B-POL/-]
A --> |Desc/Code/BHMA| G[Oil-rubbed bronze/B-ORB/613]
A --> H[etc.]
end
```
```mermaid
flowchart TD

subgraph Length selection
Q[Possible Options]
Q --> J[6]
Q --> S[6-1/8]
Q --> T[6-1/4]
Q --> U[6-3/8]
Q --> V[6-1/2]
Q --> W[6-5/8]
Q --> X[6-3/4]
Q --> Y[6-7/8]
Q --> Z[7]
Q --> ZZ[etc.]
end

```
- **Base price chart:**

![360 Series Base price Image](./images/auto_baseprice_list.png)


- **Product dependant Optional Params:**

```mermaid
flowchart TD

B[No Hole/NH]
P[Possible Options]
B --> P 
C[Light spring] --> P 
D[Security screw] --> P 
E[End Cap] --> P 
F[Pull out] --> P 
G[etc.] 
P --> Y[yes] 
P --> N[No] 
```
- **Optional price chart:**

![Adon charges Image](./images/adon_charges.png)
![Adon part charges Image](./images/adon_part_price.png)

- **Different part's Price chart:**
Parts can be treated as seperate Product.
![Adon part charges Image](./images/adon_part_price.png)
![ Parts Image-1](./images/part_price.png)