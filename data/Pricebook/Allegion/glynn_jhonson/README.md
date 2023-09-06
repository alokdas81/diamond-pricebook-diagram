### **Glynn Jhonson [GJ_Price_Book_12_Feb2023_CAN010061](./GJ_Price_Book_12_Feb2023_CAN010061.pdf):**

**Finish Codes:**
![Finish chart Image](../finish_codes.png)
```mermaid
flowchart TD

subgraph Series Selection
G[Possible Options]
70
79
81
100
J[etc.]
end


G --> 70
G --> 79
G --> 81
G --> 100
G --> J
```

- **Product dependent Required Params:**

```mermaid
graph TB


subgraph Function Selection
D[Possible Options]
E[Hold-Open/H]
F[Stop-Only/S]
H[FRICTION STOP-ONLY/F]
K[INTERNAL HOLD-OPEN/HP]
end

subgraph Model Selection
A[Possible Options]
B[70 series heavy-duty]
C[79 series extra heavy-duty]
I[450 series medium-duty]
L[etc.]
end


A --> B
A --> C
A --> I
A --> L

D --> E
D --> F
D --> H
D --> K


```
```mermaid
graph TB

subgraph Finish Selection
H[Possible Options]
605
606
612
613
619
622
625
I[etc.]
end

subgraph Size Selection
G[Possible Options]
2
3
4
5
6
L[etc.]
end

G --> 2
G --> 3
G --> 4
G --> 5
G --> 6
G --> L

H --> 605
H --> 606
H --> 612
H --> 613

H --> 619
H --> 622
H --> 625
H --> I

```

- **Base Price chart:**

![70/79 Series price Image](./images/price_list.png)
- **Optional Params:**

```mermaid
flowchart TD

A[Jamb Bracket]
B[Security Screw]
C[Sex bolts]
P[Possible Options]
A --> P 
B --> P 
C --> P 
P --> Y[yes] 
P --> N[No] 
```
```mermaid
graph TB

subgraph Optional Finish selection
F[RAL Powder-Coat finish]
end

subgraph Door Thikness Selection
A[Possible Options]
B[2]
C[2-1/4]
D[2-3/4]
E[3]
L[etc.]
end

A --> B
A --> C
A --> D
A --> E
A --> L

```
- **Optional price chart:**

![70/79 Series Options Image](./images/adon_price_list.png)


- Parts selection criteria
```mermaid
flowchart TD

A[Start] --> B[Model = 70 series heavy-duty]
 --> D[Finish 'BHMA/US Number' = 605] --> |Filter out the parts depending on the above selection| F[Possible parts are marked in red color in the following figure \n Note: This list of parts can  be different for different series]
```
- **Different part's Price chart:**
Parts can be treated as seperate Product.
![70 Series Parts Image-1](./images/part_price1.png)
![70 Series Part Image-2](./images/part_price2.png)
