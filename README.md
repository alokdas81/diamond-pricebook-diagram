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
E[Hold-Open]
F[Stop-Only]
end

subgraph Model Selection
A[Possible Options]
B[heavy-duty]
C[extra heavy-duty]
end

subgraph Series Selection
G[Possible Options]
70
79
81
100
end

A --> B
A --> C

D --> E
D --> F

G --> 70
G --> 79
G --> 81
G --> 100

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
end

G --> 2
G --> 3
G --> 4
G --> 5
G --> 6

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
end

A --> B
A --> C
A --> D
A --> E

G --> H
G --> I
G --> J
G --> K
```
- Adon price chart
![70/79 Series Options Image](images/glynn_jhonson/option_price_list.png)


- Parts selection
```mermaid
flowchart TD

A[Start] --> B[Series == 70] --> C[Model == heavy-duty]
C --> D[BHMA Finish == 605] --> E[US Number == US3] --> F[Possible parts are marked in red color in the following figure]
```
- Different part's Price chart
![70 Series Parts Image-1](images/glynn_jhonson/part_price1.png)
![70 Series Part Image-2](images/glynn_jhonson/part_price2.png)