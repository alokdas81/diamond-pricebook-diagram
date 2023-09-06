### **Falcon [CAN110065_FAL_Price_Book_13_Feb2023_RevJun2023_07-05-23](./CAN110065_FAL_Price_Book_13_Feb2023_RevJun2023_07-05-23.pdf):**
**Finish Codes:**
![Finish chart Image](../finish_codes.png)
```mermaid
flowchart TD


subgraph Series Selection
A[Possible Options]
B[MA] 
C[T]
D[D200]
E[25]
F[24]
G[etc.]
H[Locks]
I[Exit Devices]
end

A --> B
A --> C
A --> D
A --> E
A --> F
A --> G
B --> |Product Category| H
C --> |Product Category| H
D --> |Product Category| H
E --> |Product Category| I
F --> |Product Category| I

```
**1. Locks [MA series, T Series, X Series, D-200 Series etc.]:**
- **Product dependent Required Params:**

```mermaid
flowchart TD


subgraph Cylinder Selection
D[Possible Options]
P
P6
P7
G6
BB6
K[etc.]
end

subgraph Function Selection
A[Possible Options]
B[101]
C[161]
I[521]
L[etc.]
end

A --> B
A --> C
A --> I
A --> L

D --> P
D --> P6
D --> P7
D --> G6
D --> BB6
D --> K

```
```mermaid
graph TB

subgraph Rose/Escutcheon-outside style/design Selection
A[Possible Options]
LLL
GALA
B[etc.]
end

subgraph Lever-outside finish Selection
H[Possible Options]
605
606
613
619
622
625
I[etc.]
end

subgraph Lever-outside style/design Selection
J[Possible Options]
AG
LTG
AN
LTN
QG
QN
K[etc.]
end



H --> 605
H --> 606
H --> 613
H --> 619
H --> 622
H --> 625
H --> I

J --> AG
J --> LTG
J --> AN
J --> LTN
J --> QG
J --> QN
J --> K

A --> LLL
A --> GALA
A --> B
```

- **Base Price chart:**

![MA Series price Image](./images/price_list.png)


```mermaid
flowchart TD

subgraph Rose/Escutcheon-inside style/design Selection
A[Possible Options]
LLL
GALA
B[etc.]
end

subgraph Lever-inside finish Selection
H[Possible Options]
605
606
613
619
622
625
I[etc.]
end

subgraph Lever-inside style/design Selection
J[Possible Options]
AG
LTG
AN
LTN
QG
QN
K[etc.]
end


H --> 605
H --> 606
H --> 613
H --> 619
H --> 622
H --> 625
H --> I

J --> AG
J --> LTG
J --> AN
J --> LTN
J --> QG
J --> QN
J --> K

A --> LLL
A --> GALA
A --> B
```

```mermaid
graph TB


subgraph Armor front Selection
N[Possible Options]
O[S77801-LL]
P[S77804-LL]
Q[S77805-LL]
R[LLL-Less armor front]
S[etc.]
end


subgraph Latch Selection
D[Possible Options]
E[23981137]
F[24074387]
G[23981160]
H[43-005]
I[98535]
J[LLL-Less Latch]
K[etc.]
end

subgraph Strike Selection
A[Possible Options]
A8737-1
A8737-2
A8737-3
A8737-4
5185
5185-4
C[LLL-Less Strike]
B[etc.]
end

subgraph Handling Selection
L[Possible Options]
RH[Right hand/RH]
LH[Left hand/LH]
LR[Left hand reverse/LR]
RR[Righ hand reverse/RR]
M[etc.]
end

N --> O
N --> P
N --> Q
N --> R
N --> S

D --> E
D --> F
D --> G
D --> H
D --> I
D --> J
D --> K

L --> RH
L --> LH
L --> LR
L --> RR
L --> M

A --> A8737-1
A --> A8737-2
A --> A8737-3
A --> A8737-4
A --> 5185
A --> 5185-4
A --> C
A --> B
```
```mermaid
flowchart TD

subgraph Door Dimensions
A[Door Thikness]
Extended
end
```
- **Less component price list:**

![T Series less component price Image](./images/less_component_price_list.png)
- **Optional Params:**
```mermaid
flowchart TD

A[Latch Extension]
B[Box for ANSI strike]
C[Pack Cylinders loose]
D[Screw option]
E[Lead lining]
P[Possible Options]
A --> P 
B --> P 
C --> P 
D --> P 
E --> P
P --> Y[yes] 
P --> N[No] 
```
`Lead lining` depends on the `Lever-outside design`.
```mermaid
flowchart TD

P[Lever-outside design = AG/AN/DG/DN/QG/QN]
-->  |Yes| Q[Possible Options] 
Q --> Case-1
Q --> Case-2
Q --> Case-3
P --> |No| N[Not Applicable]
subgraph Case-3
G[Lever-outside design = Quantum-Lever/QG/QN] --> H[Lead lining = 9Q] --> I[Price = $359.0/lever]
end

subgraph Case-2
D[Lever-outside design = Dane-Lever/DG/DN] --> E[Lead lining = 9D] --> F[Price = $359.0/lever]
end


subgraph Case-1
A[Lever-outside design = Avalon-Lever/AG/AN] --> B[Lead lining = 9A] --> C[Price = $359.0/lever]
end

```
- **Optional price list:**

  ![T Series optional price Image](./images/adon_price_list.png)

  Optinal Params indicator
  
  ![MA Series optional indicators price Image](./images/optional_params_indicator.png)


**2. Exit Devices [25 Series, 24 Series, 2390 Series etc.]:**
- **Product dependent Required Params:**
```mermaid
graph TB

subgraph Device Finish Selection
Q[Possible Options]
Q --> 605
Q --> 606
Q --> 612
Q --> 619
Q --> 622
Q --> 625
Q --> R[etc.]
end

subgraph Rating selection
N[Possible Options] --> O[Panic exit device/ - / None]
N --> P[Fire exit device/F]
end

subgraph Function selection
G[Possible Options] --> H[Dummy Trim/DT]
G --> I[Lever dummy Trim/LDT]
G --> J[Knob dummy Trim/KDT]
G --> K[Exit Only/EO]
G --> L[Knob Night Latch/KNL]
G --> M[etc.]
end

subgraph Device-type selection
A[Prossible-Options] --> B[Rim device/R]
A --> C[Surface vertical rod/V]
A --> D[Mortise Lock/M]
A --> E[ Concealed vertical rod/C]
A --> F[Wood Door concealed vertical rod/CWDC]
end

```
```mermaid
graph TB



subgraph Device Handing Selection
E[Possible Options] --> F[Right hand reverse/RHR]
E --> G[Left hand reverse/LHR]
end

subgraph Device size Selection
A[Possible Options]
A --> B[2': 2' Device for 2' Door]
A --> C[3': 3' Device for 2'4'' to 3' Door]
A --> D[4': 4' Device for 2'10'' to 4' Door]
end

```
- **Base price chart:**

![25 Series Base price Image](./images/exit_device_base_price.png)
- **Optional Params:**
  ```mermaid
  graph TB


  subgraph Device Trim Finish Selection
  K[Possible Options]
  K --> 605
  K --> 606
  K --> 629
  K --> 695
  K --> 710
  K --> R[etc.]
  end

  subgraph Device Trim Design Selection
  A[Possible Options] --> B[Avalon/AVA]
  A --> C[Broadway/BRW]
  A --> D[Boardwalk/BRK]
  A --> E[Dane/DAN]
  A --> F[Sutro/SUT]
  A --> G[Danish/DSH]
  A --> H[Latitude/LAT]
  A --> I[Longitude/LON]
  A --> J[Quantum/QUA]
  end

  subgraph Device Trim Design Type Selection
  O[Possible Options] --> P[Standard Lever]
  O --> Q[Knurled Lever]
  end

  subgraph Device Trim Selection
  S[Possible Options] --> T[510L/Lever trim]
  S --> U[511L/Vanda-resistant lever trim]
  S --> V[L/Less trim]
  S --> W[512/Pull trim]
  S --> X[513K/Knob trim]
  S --> Y[717/Delta trim]
  end

  ```
  **Trim price chart:**

  ![25 Series trim price Image1](./images/optional_trim_price_1.png)
  ![25 Series trim price Image2](./images/optional_trim_price_2.png)

    ```mermaid
    flowchart TD


    subgraph Device Strike Selection
    A[Possible Options]
    A --> 264
    A --> 299
    A --> 3788
    A --> 2130
    A --> 1279
    A --> R[etc.]
    end
  ```
  **Strike price chart:**

  ![25 Series strike price Image](./images/optional_strike_price.png)

  

  ```mermaid
    flowchart TD

    A[Accessible]
    B[Exit Alarm]
    C[Sexbolts]
    D[SLM Blocking]
    E[GBK/Shim Kit/Risers]
    P[Possible Options]
    A --> P 
    B --> P 
    C --> P 
    D --> P 
    E --> P
    P --> Y[yes] 
    P --> N[No] 
  ```
  
  ```mermaid
  graph TB

  subgraph Dogging Selection
  G[Possible Options]
  G --> H[LD: Less Dogging]
  G --> I[CD: Cylinder Dogging]
  end

  subgraph Rods for surface/concealed Selection
  D[Possible Options]
  D --> E[LBR: Less Bottom Rod]
  D --> F[LBR-AFL: Less Bottom Rod w/Auxiliary Fire Pin]
  end

  subgraph Mortise lock Selection
  A[Possible Options]
  A --> B[LL: Less Lock]
  A --> C[8500: Standard Mortise]
  end
  ```
  
  ```mermaid
  graph TB

  subgraph Storm rating Selection
  T[Possible Options]
  T --> U[HH: Wind and Impact - Hurricane Rated]
  end

  subgraph Electrical locking Selection
  Q[Possible Options]
  Q --> R[FSA: Fail Safe]
  Q --> S[FSE: Fail Secure]
  end


  subgraph Latch Retraction Selection
  O[Possible Options]
  O --> P[MEL: Motorized Electric Latch Retraction]
  end

  subgraph Switch Selection
  J[Possible Options]
  J --> K[RX: Request to Exit Pushbar Monitor]
  J --> L[DM: Latchbolt and Pushbar Monitor]
  J --> M[DM-RX: Latchbolt and Dual Pushbar Monitor]
  J --> N[KOR: Key Bypass Switch]
  end
  ```

  ```mermaid
  graph TB

  subgraph Center line Selection
  T[Possible Options]
  T --> U[40'']
  T --> V[40-1/4'']
  T --> W[40-5/16'']
  T --> X[40-9/16'']
  T --> Y[34-1/16'']
  T --> Z[etc.]
  end
  
  
  subgraph Door Thickness Selection
  O[Possible Options]
  O --> P[DT1-3/4: 1-3/'']
  O --> Q[DT2: 2'' thickness]
  O --> R[DT2-1/4: 2-1/4'']
  end


  subgraph Door Mode Material Selection
  K[Possible Options]
  K --> L[DE: Double egress doors]
  K --> M[PR: Pair of doors]
  K --> N[SGL: Single door]
  end

  
  subgraph Frame Material Selection
  G[Possible Options]
  G --> H[ALF: Aluminum frame]
  G --> I[HMF: Hollow metal frame]
  G --> J[WDF: Wood door frame]
  end

  subgraph Door Material Selection
  A[Possible Options]
  A --> B[ALD: Aluminum door]
  A --> C[CPD: Composite door]
  A --> D[HMD: Hollow metal door]
  A --> E[WDF: Wood door frame]
  A --> F[SCDC: Steel channel door construction]
  end
  ```

  ![25 Series optional price Image1](./images/optional_price_list_1.png)
  ![25 Series optional price Image2](./images/optional_price_list_2.png)