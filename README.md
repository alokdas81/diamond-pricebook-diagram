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
          "desc": "bhma finish",
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
          "desc": "US Number",
          "code": "USN",
          "options": [
            {
              "desc": "US3",
              "code": "US3",
              "availabilityCriteria": [],
              "dependentFeatures": []
            },
            {
              "desc": "US4",
              "code": "US4",
              "availabilityCriteria": [],
              "dependentFeatures": []
            }
          ],
          "dependentFetures": []
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



# B. Different paramiter list:
Manufaturer wise PDF and their corresponding paramiter list.

## B.1 Allegion:
#### Glynn Jhonson (`GJ_Price_Book_12_Feb2023_CAN010061.pdf`):

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

subgraph BHMA Finish Selection
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

subgraph US Number Selection
J[Possible Options]
US3
US4
US10
US10B
US15
K[etc.]
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

J --> US3
J --> US4
J --> US10
J --> US10B
J --> US15
J --> K
```

- Price chart

![70/79 Series Image](images/glynn_jhonson/price_list.png)
- **Optional Params:**

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
- Adon price chart

![70/79 Series Options Image](images/glynn_jhonson/option_price_list.png)


- Parts selection criteria
```mermaid
flowchart TD

A[Start] --> B[Model = 70 series heavy-duty]
 --> D[BHMA Finish = 605] --> E[US Number = US3] --> |Filter out the parts depending on the above selection| F[Possible parts are marked in red color in the following figure \n Note: This list of parts can  be different for different series]
```
- Different part's Price chart

![70 Series Parts Image-1](images/glynn_jhonson/part_price1.png)
![70 Series Part Image-2](images/glynn_jhonson/part_price2.png)