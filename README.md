# A. Proposed DB Structure

Proposed Structure for storing the pricebook information.


```
{
  "category": "hw",
  "groupDesc": "100 series",
  "code": "100 Series",
  "products": [
    {
      "desc": "100 Series overhead concealed",
      "code": "10",
      "features": [
        {
          "desc": "bhma Number/US Number of finish",
          "code": "finish",
          "options": [
            {
              "desc": "605",
              "code": "605",
              "availabilityCriteria": [],
              "dependentFeatures": []
            },
            {
              "desc": "606",
              "code": "606",
              "availabilityCriteria": [],
              "dependentFeatures": []
            }
          ],
          "dependentFetures": [],
        },
        {
          "desc": "size",
          "code": "size",
          "options": [
            {
              "desc": "size-2",
              "code": "2",
              "availabilityCriteria": [],
              "dependentFeatures": []
            },
            {
              "desc": "size-3",
              "code": "3",
              "availabilityCriteria": [],
              "dependentFeatures": []
            }
          ],
          "dependentFetures": []
        },
        {
          "desc": "Funtion",
          "code": "Function",
          "options": [
            {
              "desc": "Hold-Open",
              "code": "H",
              "availabilityCriteria": [],
              "dependentFeatures": []
            },
            {
              "desc": "Stop-Only",
              "code": "S",
              "availabilityCriteria": [],
              "dependentFeatures": []
            }
          ],
          "dependentFetures": []
        }
      ],
      "priceList": [
        {
          "desc": "10,size 1, Hold-Open, 605 BHMA Finish, US3 US Number",
          "code": "10-1-H-605-US3",
          "pricePerQuantity": [
            {
                "unit": "Piece",
                "price": 513
            }
          ],
        },
        {
          "desc": "10,size 1,Stop-Only, 605 BHMA Finish, US3 US Number",
          "code": "10-1-S-605-US3",
          "pricePerQuantity": [
            {
                "unit": "Piece",
                "price": 513
            }
          ]
        }
      ],
      "adonFeatures": [
        {
          "desc": "suffix",
          "code": "suffix",
          "options": [
            {
              "desc": "Stop-Only function for use with Single point hold-open electronic closers.",
              "code": "SE",
              "pricePerQuantity": [
                {
                    "unit": "Piece",
                    "price": 40
                }
              ],
              "availabilityCriteria": [],
              "dependentFeatures": []
            },
            {
              "desc": "Adjustable jamb bracket available on models 103-106 (Allows for field adjustment of Hold-Open 85° - 110°)",
              "code": "ADJ",
              "pricePerQuantity": [
                {
                    "unit": "Piece",
                    "price": 92
                }
              ],
              "availabilityCriteria": [
                {
                    "featureCode": "size",
                    "featureOptions": ["3","4","5","6"]
                }],
              "dependentFeatures": []
            }
          ],
          "dependentFetures": []
        }
      ]
    }
  ]
}
```

The above structure has been generated depending on the following files.
###### **Allegion**:
`GJ_Price_Book_12_Feb2023_CAN010061.pdf`,
`CAN110065_FAL_Price_Book_13_Feb2023_RevJun2023_07-05-23.pdf`,
`SCH_Residential_Price_Book_13_MRCAN1000.pdf`,
`CAN110962_Zero_Price_Book_10_Feb2023_RevJun2023_07-05-23.pdf`,
###### **KNC**:
`KNC - Price Book - Feb 26, 2023 18% Surcharge.pdf`
###### **NGP**:
`NGP - Price Book 2023.pdf`



# **B. Different paramiter list:**
Manufaturer wise PDF and their corresponding paramiter list.

## **B.1 Allegion:**
- Need to follow the common coding format for some parameters.
![finish code list](./images/Allegion/finish_codes.png)
#### **B.1.a Glynn Jhonson (`GJ_Price_Book_12_Feb2023_CAN010061.pdf`):**

- **Required Params:**

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

subgraph Series Selection
G[Possible Options]
70
79
81
100
J[etc.]
end

A --> B
A --> C
A --> I
A --> L

D --> E
D --> F
D --> H
D --> K

G --> 70
G --> 79
G --> 81
G --> 100
G --> J

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

![70/79 Series price Image](images/Allegion/glynn_jhonson/price_list.png)
- **Adon Params:**

```mermaid
graph TB



subgraph Different Parts selection
G[Possible Options]
H[Door bracket and pin]
I[Jamb bracket]
J[Angle jamb bracket kit]
K[etc.]
end

subgraph Optional Finish selection
F[RAL Powder-Coat finish]
end

subgraph suffix Selection
A[Possible Options]
B[J]
C[SNB-1]
D[SNB-2]
E[SOC]
L[etc.]
end

A --> B
A --> C
A --> D
A --> E
A --> L

G --> H
G --> I
G --> J
G --> K
```
- **Adon price chart:**

![70/79 Series Options Image](images/Allegion/glynn_jhonson/adon_price_list.png)


- Parts selection criteria
```mermaid
flowchart TD

A[Start] --> B[Model = 70 series heavy-duty]
 --> D[Finish = 605] --> E[US Number = US3] --> |Filter out the parts depending on the above selection| F[Possible parts are marked in red color in the following figure \n Note: This list of parts can  be different for different series]
```
- **Different part's Price chart:**

![70 Series Parts Image-1](images/Allegion/glynn_jhonson/part_price1.png)
![70 Series Part Image-2](images/Allegion/glynn_jhonson/part_price2.png)

#### **B.1.b Falcon (`CAN110065_FAL_Price_Book_13_Feb2023_RevJun2023_07-05-23.pdf`):**

```mermaid
flowchart TD


subgraph Product Category Selection
A[Possible Options]
B[Locks]
D[EXit Devices]
E[Electronics]
F[etc.]
end


A --> B
A --> D
A --> E
A --> F
```
**1. Locks:**
- **Product dependent Required Params:**

```mermaid
flowchart TD

subgraph Series Selection
G[Possible Options]
MA
T
X
D200
J[etc.]
end

G --> MA
G --> T
G --> X
G --> D200
G --> J

subgraph Cylinder Selection
D[Possible Options]
P
P6
P7
G6
BB6
K[etc.]
end

subgraph Series + Function Selection
A[Possible Options]
B[MA101]
C[MA161]
I[MA521]
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

![MA Series price Image](images/Allegion/falcon/price_list.png)


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

![T Series less component price Image](images/Allegion/falcon/less_component_price_list.png)
- **Adon Params:**
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
- **Adon price list:**

![T Series optional price Image](images/Allegion/falcon/adon_price_list.png)

**2. Exit Devices:**
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

![25 Series Base price Image](images/Allegion/falcon/exit_device_base_price.png)
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

  ![25 Series trim price Image1](images/Allegion/falcon/optional_trim_price_1.png)
  ![25 Series trim price Image2](images/Allegion/falcon/optional_trim_price_2.png)

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

  ![25 Series strike price Image](images/Allegion/falcon/optional_strike_price.png)



```mermaid
flowchart TD


subgraph Exit-devices
A[work in progress...]
end


```



