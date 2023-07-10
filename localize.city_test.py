import json
import pandas as pd

#Testing Process to Read API from Developer Page 

localize_json_string = """{
    "data": {
        "searchResult": {
            "groupId": "452001315",
            "airflowGenerationId": "202305150920001",
            "total": 4515,
            "totalNearby": 1083,
            "lastInGeometryId": "l-a38u1cagfonq",
            "poi": [
                {
                    "id": "l-64cmehbu9721",
                    "locationPoint": {
                        "lat": 40.690948486328125,
                        "lng": -73.98236083984375,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-13T00:33:55.324Z",
                    "addressDetails": {
                        "docId": "55-fleet-street-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11201",
                        "streetName": "fleet street",
                        "neighbourhood": "downtown brooklyn",
                        "neighbourhoodDocId": "downtown-brooklyn-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "55",
                        "unitNumber": "27K",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 55,
                    "address": "55 Fleet Street, Brooklyn, New York",
                    "beds": 1,
                    "area": null,
                    "price": 4465,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Washer/dryer",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-laundry",
                            "groupTypeForLabels": "amenities.unit-laundry",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 4465,
                            "date": "2023-05-13T00:37:51.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": "condo",
                    "images": [
                        {
                            "imageUrl": "bulletins2/2971dcc3c5b120767df5a07abd0cec74.jpg",
                            "isFloorplan": true,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/e0a72a7287773c09765e86a389bad672.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/23c1ab3738352d59d9bae7480cb73bfe.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/684ab36ecb069da630ab7b063c8cc671.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/8d0a46e478ee4a16e3b0e6d5c1312481.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/186f697c407fcfeda6712668379be809.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "rebny",
                    "originalId": "RPLU-5122469838",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Above average crime rate",
                                    "tagLine": "CRIME",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Building sits along truck route",
                                    "tagLine": "ON A TRUCK ROUTE",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "planning",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Construction site next door",
                                    "tagLine": "CONSTRUCTION COMING",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Lots of complaints about noise nearby",
                                    "tagLine": "NOISY AREA",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "livability",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Limited park access",
                                    "tagLine": "",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Dangerous intersection nearby",
                                    "tagLine": "ROAD SAFETY ISSUE",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-dnpv3kp8abu2",
                    "locationPoint": {
                        "lat": 40.70037841796875,
                        "lng": -73.99414825439453,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-06-10T00:38:35.651Z",
                    "addressDetails": {
                        "docId": "29-willow-street-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11201",
                        "streetName": "willow street",
                        "neighbourhood": "brooklyn heights",
                        "neighbourhoodDocId": "brooklyn-heights-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "29",
                        "unitNumber": "2R",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 27,
                    "address": "29 Willow Street, Brooklyn, New York",
                    "beds": 2,
                    "area": null,
                    "price": 7750,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Washer/dryer",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-laundry",
                            "groupTypeForLabels": "amenities.unit-laundry",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 7750,
                            "date": "2023-06-10T00:42:00.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": "rental unit",
                    "images": [
                        {
                            "imageUrl": "bulletins2/c276911d4bb9928014532ab363d11250.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/a3530e39b5599a82d773df1968f88578.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/846004d1bcd046b67575fee9480875d8.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/42d9d18b800d9d8cbbd3813475811929.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/cc2760f7b6d50cf1d5262299c1e5aefd.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/1c351ea752f447bf8a43b008359879ee.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/11d8d0f16e1ada9896a3bd62e60e95fd.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/126af1612013f60859b1c1fd784cdd1b.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "rebny",
                    "originalId": "RPLU-33422525958",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Below average crime rate",
                                    "tagLine": "CRIME",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "planning",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Historic District - costs & restrictions",
                                    "tagLine": "HISTORIC DISTRICT",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Lots of complaints about noise nearby",
                                    "tagLine": "NOISY AREA",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "livability",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Limited park access",
                                    "tagLine": "",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Next to a highway",
                                    "tagLine": "NEXT TO HIGHWAY",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-vkhdtnq6trpi",
                    "locationPoint": {
                        "lat": 40.69236373901367,
                        "lng": -73.96131896972656,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-12T20:34:55.938Z",
                    "addressDetails": {
                        "docId": "249-willoughby-avenue-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11205",
                        "streetName": "willoughby avenue",
                        "neighbourhood": "clinton hill",
                        "neighbourhoodDocId": "clinton-hill-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "249",
                        "unitNumber": "16A",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 55,
                    "address": "249 Willoughby Avenue, Brooklyn, New York",
                    "beds": 1,
                    "area": null,
                    "price": 3688,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 3688,
                            "date": "2023-05-12T20:38:27.000Z",
                            "__typename": "EventUpdate"
                        },
                        {
                            "eventType": "delete",
                            "price": 3688,
                            "date": "2023-06-14T00:25:07.000Z",
                            "__typename": "EventUpdate"
                        },
                        {
                            "eventType": "new",
                            "price": 3688,
                            "date": "2023-06-27T02:00:26.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": "condo",
                    "images": [
                        {
                            "imageUrl": "bulletins2/956b54432c3b22480029671ff768740e.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/d1e8f66c160a3b35ff364b4baafada46.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/929f187ed878e7e6921a203c0e18892b.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/d548a05337fc7ce0eb2d15d9a5710580.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/b2effd31495849b110a790be00a899ee.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/1b18f56ad52f88eb6a446f624ad1aaf0.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/f6755ed960b617cfc1477eb4152fae0c.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/9742212ed23c455cda9a21f5019e9d91.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/bb37611948b0105ef198f645d0b80346.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/419def5d5f23787fec8af14fdd38ce2f.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/7a4e1ddb5ccbaee2515462901106a1ad.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/77308631b0461c0cd640382a72b13dba.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/8d98c7abf35a1c466f499bff11421c7b.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/fdbe68957048c094afb9e2f9889fdc64.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/5f92dcaf53e036bea7e04afd1d89b41f.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/96a325b5cae19b54d1a1798debe75f22.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/aae670b3df6925146a0429dfc38abd03.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/102028777fa33605581275d4b0a223d3.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/d82bd3afb9ab84ba3f2944c6bada86bc.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/c7965a68f811707589edfb6dcb089a22.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/88767ac1302277660b272da0b32e4d1a.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/87f5678ffe90aedddbb2620822ca9f4f.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/e1877d0ec85ea895ee34221a69570196.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/95d6628688c833dbf0098d0d4bae07ca.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/4c45d70b47cef5ba362b6d6a26b63548.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/4163cf3e928ff4179d4605c6f0be0b7d.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/c5d02ef23bb63927d19a78f855e6cb46.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/a4eb5181314b4b30810315e2fc37061b.png",
                            "isFloorplan": true,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/3dcd89bc26687f990c7ecb26fe98937b.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/5a19fd762e694f5d7c5429dfa0bb9780.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/edf0980111226c394cbd7f0708f45b9a.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/3d8db24b57ca7c7f3f109fe82e07513d.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/b9025ea0e67c9b3941d073d489fde4d6.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "rebny",
                    "originalId": "RPLU-33422469377",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Average crime rates",
                                    "tagLine": "CRIME",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Broken elevator reported",
                                    "tagLine": "ELEVATOR ISSUES",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-cecfqibkn7i1",
                    "locationPoint": {
                        "lat": 40.647342681884766,
                        "lng": -73.95297241210938,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-11T00:26:11.312Z",
                    "addressDetails": {
                        "docId": "120-veronica-place-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11226",
                        "streetName": "veronica place",
                        "neighbourhood": "flatbush",
                        "neighbourhoodDocId": "flatbush-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "120",
                        "unitNumber": "",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 57,
                    "address": "120 Veronica Place, Brooklyn, New York",
                    "beds": 4,
                    "area": 1000,
                    "price": 3200,
                    "pricesEstimations": {
                        "initialPrice": 3200,
                        "estimatedPrice": 3800,
                        "boundaries": {
                            "topBoundary": 4300,
                            "bottomBoundary": 3300,
                            "__typename": "PricesEstimationsBoundaries"
                        },
                        "__typename": "PricesEstimations"
                    },
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Elevator",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.elevator",
                            "groupTypeForLabels": "amenities.elevator",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Air conditioner",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.air-conditioner",
                            "groupTypeForLabels": "amenities.air-conditioner",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": null,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 3200,
                            "date": "2023-05-11T00:29:05.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": "three-family home",
                    "images": [
                        {
                            "imageUrl": "bulletins2/dcfb1e0c46f2b79c2f4ef6bf1db854f4.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/55764cb6a5a1aa67b0128a8ab2de0946.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/30cd2218b157b558ccd164cc64134ad9.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/34c8ebb9a1bb360d56e467733289495f.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/0be08548f250e92b3e5ef9653f85051e.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/ac6ad6e7cb23848f1fa2abd9d5e1c15d.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/6d15a6cb16ceb1e67051677ac7d8ad39.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/dae385d65cf550652f79d20e5de6f2d6.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/7aaa2305e988bfbf7b30871ce09cb215.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/cc91dc18d579ca0da773f7ce3cb1dea6.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "listhub",
                    "originalId": "3yd-MLSLINY-3477244",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Above average crime rate",
                                    "tagLine": "CRIME",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "prices",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Price is 16% lower than similar listings!",
                                    "tagLine": "LOW PRICE",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "livability",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Good park access",
                                    "tagLine": "",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Dangerous intersection nearby",
                                    "tagLine": "ROAD SAFETY ISSUE",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-8k3bbouk6ann",
                    "locationPoint": {
                        "lat": 40.68080520629883,
                        "lng": -73.92765045166016,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-13T00:33:55.334Z",
                    "addressDetails": {
                        "docId": "185-chauncey-street-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11233",
                        "streetName": "chauncey street",
                        "neighbourhood": "bedford stuyvesant",
                        "neighbourhoodDocId": "bedford-stuyvesant-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "185",
                        "unitNumber": "3F",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 55,
                    "address": "185 Chauncey Street, Brooklyn, New York",
                    "beds": 2,
                    "area": null,
                    "price": 4000,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Washer/dryer",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-laundry",
                            "groupTypeForLabels": "amenities.unit-laundry",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Air conditioner",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.air-conditioner",
                            "groupTypeForLabels": "amenities.air-conditioner",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 4800,
                            "date": "2023-05-13T00:36:08.000Z",
                            "__typename": "EventUpdate"
                        },
                        {
                            "eventType": "priceDrop",
                            "price": 4250,
                            "date": "2023-05-25T00:26:45.000Z",
                            "__typename": "EventUpdate"
                        },
                        {
                            "eventType": "priceDrop",
                            "price": 4000,
                            "date": "2023-06-16T04:40:51.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [
                        {
                            "from": "2023-06-18T15:00:00.000Z",
                            "to": "2023-06-18T15:30:00.000Z",
                            "__typename": "OpenHouse"
                        }
                    ],
                    "buildingClass": "rental unit",
                    "images": [
                        {
                            "imageUrl": "bulletins2/39348535f82a0a999672313e70ed9748.jpg",
                            "isFloorplan": true,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/2a2a26ec8688b5e6a80c31e8ea193338.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/9d20e434a65be140b1ca071dacdd67c0.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/3038fa43fa46ae1155bf326a2a50677b.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/d33a694621abd8d11a29b22a299ee9a3.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/6597c241fd518299641cc9840e666a4a.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/bf2b9d47b5af94eb3f44eda4ea5a05b7.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/b90f035569a0f9d839c9a405b3997b9d.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/7d25ff0aadea532962d4c9cc67d91d31.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/c27842640a135baf2696057564e90a8b.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/b5e3259f8a159d0c97a73a823c45d110.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/3b24c5c061530c8c8868b803e65061c4.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/10df806068ae7f3ddbf142e5156be035.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/be6305e01c2f748e2f5082506a0b3fb1.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": 573,
                    "source": "rebny",
                    "originalId": "OLRS-2036965",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Slightly above average crime rate",
                                    "tagLine": "CRIME",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "naturalLight",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "This apartment has moderate sunlight",
                                    "tagLine": "",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "planning",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Near Historic District - less restrictions",
                                    "tagLine": "NEAR HISTORIC DISTRICT",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Lots of complaints about noise nearby",
                                    "tagLine": "NOISY AREA",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "planning",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Bldg’s view could be cut off in the future",
                                    "tagLine": "VIEW TO BE BLOCKED",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-2k3uv7jiag7s",
                    "locationPoint": {
                        "lat": 40.70285415649414,
                        "lng": -73.98348236083984,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-13T04:24:07.256Z",
                    "addressDetails": {
                        "docId": "260-water-street-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11201",
                        "streetName": "water street",
                        "neighbourhood": "vinegar hill",
                        "neighbourhoodDocId": "vinegar-hill-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "260",
                        "unitNumber": "1D",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 55,
                    "address": "260 Water Street, Brooklyn, New York",
                    "beds": 1,
                    "area": null,
                    "price": 4195,
                    "pricesEstimations": {
                        "initialPrice": 4195,
                        "estimatedPrice": 3800,
                        "boundaries": {
                            "topBoundary": 4000,
                            "bottomBoundary": 3600,
                            "__typename": "PricesEstimationsBoundaries"
                        },
                        "__typename": "PricesEstimations"
                    },
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Washer/dryer",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-laundry",
                            "groupTypeForLabels": "amenities.unit-laundry",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Laundry in building",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.building-laundry",
                            "groupTypeForLabels": "amenities.building-laundry",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 4195,
                            "date": "2023-05-13T04:27:25.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": "rental unit",
                    "images": [
                        {
                            "imageUrl": "bulletins2/10b47e71f3ea30b9b278b1c911ba2a54.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/dc4556f41234f17b032359e1334dfd18.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/c2190e6452d7ca1edb757ff342073cf7.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/2e46a1a62fc3059ff6086a0879977094.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/4e2b4973a0ebf647a9e461f6be7f40e2.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/ec3b1eb903d6fc7d7a451f0891c2abbb.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/cfc2cc43b527adcb417069eadd5fce83.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/9e51baeedfda72a444186079aa7d58fa.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/8ac777fe8ad11f651144d5f932b21ecf.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "rebny",
                    "originalId": "RLMX-89355",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Average crime rates",
                                    "tagLine": "CRIME",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "planning",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Construction site next door",
                                    "tagLine": "CONSTRUCTION COMING",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "planning",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Near Historic District - less restrictions",
                                    "tagLine": "NEAR HISTORIC DISTRICT",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Lots of complaints about noise nearby",
                                    "tagLine": "NOISY AREA",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "prices",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Price is 10% higher than similar listings!",
                                    "tagLine": "HIGH PRICE",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "livability",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Limited park access",
                                    "tagLine": "",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "planning",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Bldg’s view could be cut off in the future",
                                    "tagLine": "VIEW TO BE BLOCKED",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-5cmrftkb5p0l",
                    "locationPoint": {
                        "lat": 40.71467971801758,
                        "lng": -73.95896911621094,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-12T12:18:37.047Z",
                    "addressDetails": {
                        "docId": "658-driggs-avenue-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11211",
                        "streetName": "driggs avenue",
                        "neighbourhood": "williamsburg",
                        "neighbourhoodDocId": "williamsburg-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "658",
                        "unitNumber": "2E",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": null,
                    "dealType": "unitRent",
                    "daysOnMarket": 56,
                    "address": "658 Driggs Avenue, Brooklyn, New York",
                    "beds": 1,
                    "area": null,
                    "price": 6150,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Balcony",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.balcony",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Terrace",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.terrace",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Patio",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.patio",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Roofdeck",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.roof-deck",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Garden",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garden",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Courtyard",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.courtyard",
                            "groupTypeForLabels": "amenities.shared_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "City views",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.city-view",
                            "groupTypeForLabels": "amenities.views",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Park views",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.park-view",
                            "groupTypeForLabels": "amenities.views",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.health-club",
                            "groupTypeForLabels": "amenities.health-club",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Fireplace",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.fireplace",
                            "groupTypeForLabels": "amenities.fireplace",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Doorman",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.doorman",
                            "groupTypeForLabels": "amenities.doorman",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Building garden",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.building-garden",
                            "groupTypeForLabels": "amenities.shared_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Concierge",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.concierge",
                            "groupTypeForLabels": "amenities.concierge",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.fitness-room",
                            "groupTypeForLabels": "amenities.fitness-room",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Elevator",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.elevator",
                            "groupTypeForLabels": "amenities.elevator",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Air conditioner",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.air-conditioner",
                            "groupTypeForLabels": "amenities.air-conditioner",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Building terrace",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.building-patio",
                            "groupTypeForLabels": "amenities.shared_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Building terrace",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.building-terrace",
                            "groupTypeForLabels": "amenities.shared_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Bike storage",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.bike-storage",
                            "groupTypeForLabels": "amenities.bike-storage",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": null,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 6150,
                            "date": "2023-05-12T12:19:06.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": null,
                    "images": [
                        {
                            "imageUrl": "bulletins2/957bb77b55a40cc09c19867785ddc4e1.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/be5d5023858e1045976c445ace4e45c9.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/aca6f6c243023ec8951ebbf60ab93edc.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/434610d2bdaeb75e26b411c0a8c5a986.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/3201071d3ca0331233178dc2e4c7ddc8.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/e8a6f610ef27af97242510f3cbf41e43.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/55ea4091d1ec6085bb707e55556e5688.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/05cdc38467d25390314ac575b2f1747b.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "realtymx",
                    "originalId": "livingny_134600",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Average crime rates",
                                    "tagLine": "CRIME",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Building sits along truck route",
                                    "tagLine": "ON A TRUCK ROUTE",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "planning",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Construction site next door",
                                    "tagLine": "CONSTRUCTION COMING",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "planning",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Near Historic District - less restrictions",
                                    "tagLine": "NEAR HISTORIC DISTRICT",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-ksagliggun2m",
                    "locationPoint": {
                        "lat": 40.68238067626953,
                        "lng": -73.9070816040039,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-10T16:21:57.963Z",
                    "addressDetails": {
                        "docId": "37-furman-avenue-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11207",
                        "streetName": "furman avenue",
                        "neighbourhood": "bushwick",
                        "neighbourhoodDocId": "bushwick-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "37",
                        "unitNumber": "",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 57,
                    "address": "37 Furman Avenue, Brooklyn, New York",
                    "beds": 3,
                    "area": 1140,
                    "price": 2900,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Elevator",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.elevator",
                            "groupTypeForLabels": "amenities.elevator",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": null,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 2900,
                            "date": "2023-05-10T16:22:30.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": "three-family home",
                    "images": [
                        {
                            "imageUrl": "bulletins2/e4e76d9f899e47ecef34bdd364de7f04.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/fcff36f90dd63dceccb80d1bd719436a.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/feafe472b4e641a71b97f9de04bad17d.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/867af9c4e05f4e9056f08efa61aef388.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/4fad2abac6992c7ff8dbc895c1ced3d4.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/bf4bf8460eb3cf6d5b854bbd2dc68447.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/4af56a80bae41bc9723754f0e98cbb5f.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/8b6b8489bf43b4d21a5b8b4f41d9f8ad.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/a71f7cd403c9cd8f54684ee378e1b419.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "listhub",
                    "originalId": "3yd-BMLSNY-473917",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Above average crime rate",
                                    "tagLine": "CRIME",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "prices",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Only 3 similar listings under $3.3K!",
                                    "tagLine": "PRICE OPPORTUNITY",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-of63m38nnbqu",
                    "locationPoint": {
                        "lat": 40.68565368652344,
                        "lng": -73.90975189208984,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2022-03-10T16:22:23.945Z",
                    "addressDetails": {
                        "docId": "71-cooper-avenue-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11207",
                        "streetName": "cooper street",
                        "neighbourhood": "bushwick",
                        "neighbourhoodDocId": "bushwick-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "71",
                        "unitNumber": "2A",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": null,
                    "dealType": "unitRent",
                    "daysOnMarket": 57,
                    "address": "71 Cooper Street, Brooklyn, New York",
                    "beds": 0,
                    "area": null,
                    "price": 2085,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Patio",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.patio",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Terrace",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.terrace",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Garden",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garden",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Courtyard",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.courtyard",
                            "groupTypeForLabels": "amenities.shared_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Balcony",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.balcony",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Roofdeck",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.roof-deck",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Park views",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.park-view",
                            "groupTypeForLabels": "amenities.views",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "City views",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.city-view",
                            "groupTypeForLabels": "amenities.views",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.fitness-room",
                            "groupTypeForLabels": "amenities.fitness-room",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Concierge",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.concierge",
                            "groupTypeForLabels": "amenities.concierge",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Fireplace",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.fireplace",
                            "groupTypeForLabels": "amenities.fireplace",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Doorman",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.doorman",
                            "groupTypeForLabels": "amenities.doorman",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.health-club",
                            "groupTypeForLabels": "amenities.health-club",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Building garden",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.building-garden",
                            "groupTypeForLabels": "amenities.shared_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Elevator",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.elevator",
                            "groupTypeForLabels": "amenities.elevator",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Building terrace",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.building-terrace",
                            "groupTypeForLabels": "amenities.shared_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Building terrace",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.building-patio",
                            "groupTypeForLabels": "amenities.shared_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Bike storage",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.bike-storage",
                            "groupTypeForLabels": "amenities.bike-storage",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": null,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 1550,
                            "date": "2022-03-10T16:22:31.000Z",
                            "__typename": "EventUpdate"
                        },
                        {
                            "eventType": "priceUp",
                            "price": 1599,
                            "date": "2022-03-18T15:31:33.000Z",
                            "__typename": "EventUpdate"
                        },
                        {
                            "eventType": "delete",
                            "price": 1599,
                            "date": "2022-05-17T00:19:46.000Z",
                            "__typename": "EventUpdate"
                        },
                        {
                            "eventType": "new",
                            "price": 2085,
                            "date": "2022-07-19T12:16:50.000Z",
                            "__typename": "EventUpdate"
                        },
                        {
                            "eventType": "delete",
                            "price": 2085,
                            "date": "2022-09-17T00:16:42.000Z",
                            "__typename": "EventUpdate"
                        },
                        {
                            "eventType": "new",
                            "price": 2085,
                            "date": "2023-05-11T12:18:44.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": "condo",
                    "images": [
                        {
                            "imageUrl": "bulletins2/13739f59bed4af11a99ab266367788c8.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/958ca1563af0532e130b41a96fb245fe.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/98e8caedf0619d35f9411353212fc103.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/daac8559fdee42addacc503f22e8a4b6.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/ec591b5c4e9291907614437f40e0afb1.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "realtymx",
                    "originalId": "Bruma_3064",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Above average crime rate",
                                    "tagLine": "CRIME",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Building sits along truck route",
                                    "tagLine": "ON A TRUCK ROUTE",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "livability",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Good park access",
                                    "tagLine": "",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "3 Open Violations in building",
                                    "tagLine": "BLDG VIOLATIONS",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-ed3e7k8j2u13",
                    "locationPoint": {
                        "lat": 40.67937088012695,
                        "lng": -73.99369049072266,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-12T20:34:55.950Z",
                    "addressDetails": {
                        "docId": "288-carroll-street-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11231",
                        "streetName": "carroll street",
                        "neighbourhood": "gowanus",
                        "neighbourhoodDocId": "gowanus-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "288",
                        "unitNumber": "TH",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 55,
                    "address": "288 Carroll Street, Brooklyn, New York",
                    "beds": 4,
                    "area": 3100,
                    "price": 19500,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Patio",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.patio",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Terrace",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.terrace",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Washer/dryer",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-laundry",
                            "groupTypeForLabels": "amenities.unit-laundry",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 19500,
                            "date": "2023-05-12T20:35:47.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": "single-family home",
                    "images": [
                        {
                            "imageUrl": "bulletins2/09f70df63cd8efdbd1d9564700317ef3.jpg",
                            "isFloorplan": true,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/8b6fc14a1a785ccc5ecace28b6eea925.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/e18f8c6bf2b398cd6b5bb04cd10681fb.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/0a239f6164156e69dc7af92e64739d58.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/85d8ba30c06630624b12dea326627e54.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/acda92048dca258175c3a7c9cca30838.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/de995d0ce50109e0a155c1588a49d8ce.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/ae80d371cb8c686c58099e8c4e2d2909.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/9b147b76ffaf643ce37176189ad58642.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/90f782a11a0fb33e1d3fb7a2dd967941.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/f51cd6fca37cddecf2dbe69c7c7dfe64.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/3e8360cf15784ad2cefa7a731ab79881.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/1295e99cf192b433183151373c37c5f7.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/2a6fd027d0a23dd527bca198dd39bab5.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/3f7fa9342817cc6fa6ff3c4f6f63cf3f.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/04b401d1912019bca56be70359c3a669.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/9c94df853d5c1f38ed311251175aabb2.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "rebny",
                    "originalId": "OLRS-00011925402",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Below average crime rate",
                                    "tagLine": "CRIME",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "planning",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Historic District - costs & restrictions",
                                    "tagLine": "HISTORIC DISTRICT",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "livability",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Good park access",
                                    "tagLine": "",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-455trmvui20s",
                    "locationPoint": {
                        "lat": 40.710716247558594,
                        "lng": -73.94863891601562,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-11T20:32:46.827Z",
                    "addressDetails": {
                        "docId": "462-lorimer-street-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11206",
                        "streetName": "lorimer street",
                        "neighbourhood": "williamsburg",
                        "neighbourhoodDocId": "williamsburg-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "462",
                        "unitNumber": "1",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 56,
                    "address": "462 Lorimer Street, Brooklyn, New York",
                    "beds": 1,
                    "area": 650,
                    "price": 3995,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Washer/dryer",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-laundry",
                            "groupTypeForLabels": "amenities.unit-laundry",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 3995,
                            "date": "2023-05-11T20:34:58.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [
                        {
                            "from": "2023-05-21T12:00:00.000Z",
                            "to": "2023-05-21T13:00:00.000Z",
                            "__typename": "OpenHouse"
                        }
                    ],
                    "buildingClass": "two-family home",
                    "images": [
                        {
                            "imageUrl": "bulletins2/4a3931f15832b18f6f19335172733d4e.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/f3c998ff7a88627acad4b9198cf733d3.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/b6f95769a323acd7052ea538240f3d55.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/58e43b0c0e0970a9d21000bd2f4c4e2b.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/497dd4c01b1a282d635430e474d9fafa.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/393ca669baf41c771c480f6b50333449.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/267d74924e64604bc1695bd15a4abdcb.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/0634f7d68b8789081feb0a448fae3e5b.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/6790ce156dd717366825292ae0b23e47.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/5ae563266e605011c8210a6d4deb4268.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "rebny",
                    "originalId": "OLRS-2036629",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Average crime rates",
                                    "tagLine": "CRIME",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "naturalLight",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "This apartment has moderate sunlight",
                                    "tagLine": "",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "livability",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Good park access",
                                    "tagLine": "",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "prices",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "350 sq ft less than similar listings.",
                                    "tagLine": "LESS SQ FT",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Dangerous intersection nearby",
                                    "tagLine": "ROAD SAFETY ISSUE",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-k9kpg8j17iqj",
                    "locationPoint": {
                        "lat": 40.714195251464844,
                        "lng": -73.96483612060547,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-12T04:28:50.008Z",
                    "addressDetails": {
                        "docId": "74-south-2-street-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11249",
                        "streetName": "south 2 street",
                        "neighbourhood": "williamsburg",
                        "neighbourhoodDocId": "williamsburg-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "74",
                        "unitNumber": "NA",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 56,
                    "address": "74 South 2 Street, Brooklyn, New York",
                    "beds": 4,
                    "area": 3200,
                    "price": 22000,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Washer/dryer",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-laundry",
                            "groupTypeForLabels": "amenities.unit-laundry",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 25000,
                            "date": "2023-05-12T04:32:18.000Z",
                            "__typename": "EventUpdate"
                        },
                        {
                            "eventType": "priceDrop",
                            "price": 22000,
                            "date": "2023-06-06T20:33:37.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [
                        {
                            "from": "2023-07-09T12:00:00.000Z",
                            "to": "2023-07-09T13:00:00.000Z",
                            "__typename": "OpenHouse"
                        }
                    ],
                    "buildingClass": "rental unit",
                    "images": [
                        {
                            "imageUrl": "bulletins2/2c33a60221866d7eb7d8255c7d219f69.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/aeca9b99c2d413bc5e2ad84f6439cc7a.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/fbdba28fb91a3f8278feb348934e9781.png",
                            "isFloorplan": true,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/5d08b273bf3252cc9d3ec5e41ca528e6.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/2bd1e639f3a64d2408d2279b35e96097.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/e160020217d754f007eab18ccecb05b7.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/5b54cbcfdbdcd54941e179c7f5f35071.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/f4f808911a27bb429ac6daff3f58c87f.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/0d96ad53a674e3db182e1896d8d3743f.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/8628c4235c6711b3d480a9f83239914e.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/0b0d3b7799b61fb572c362f644071d8c.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/6da43104c7b5a9cdf5978d9ee6ed5b5b.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/f94cc522911c778ffc29fcede9257c9c.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/678f38f06e13acf8a2b2284eb63be6fb.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/3e2cacdd442be85cd5e68dc269e7e0a6.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/b7fe1e35d71dacd41d6b45b9719defbf.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/7de2ad810e0f46af2cca87645de6a0a5.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/210d1b11521e5243c5a31951c74f35ae.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/32eaa629587cfbf5905a39c1b362b8bc.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/fa0c0df9aa2ba6467214f794bf36018c.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/5246b8afc19a2c08fffc0c269e91d571.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/1361fa2fafce1d4db506d5f24b957603.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/975833adea014417295ae7399275e530.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/98aae0b7bd4c45ccad52837bfba9f026.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/c41dae5558d3f05d6f2c4f7b10f4b262.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/d14c75767a40cb829b7b97556a1921fb.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/93c63669cb0083ad59f968890be8df3c.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/fda5f833c6859d19f695e4db7f8042eb.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/8d451b0053d1e7b891daec90e501a837.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/454151346ae924701c601c972b7d8ed6.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/3f80aebc2ad59d5bd60ae4963830eb99.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/6279ad196016ad8f259f969b27a07257.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/629aab6d71c0bd2ea84117740941443f.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "rebny",
                    "originalId": "RPLU-33422467679",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Average crime rates",
                                    "tagLine": "CRIME",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-jffqhnkl3lrs",
                    "locationPoint": {
                        "lat": 40.68490982055664,
                        "lng": -73.97854614257812,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-10T20:29:58.892Z",
                    "addressDetails": {
                        "docId": "560-state-street-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11217",
                        "streetName": "state street",
                        "neighbourhood": "boerum hill",
                        "neighbourhoodDocId": "boerum-hill-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "560",
                        "unitNumber": "3B",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 57,
                    "address": "560 State Street, Brooklyn, New York",
                    "beds": 2,
                    "area": 1070,
                    "price": 5900,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Washer/dryer",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-laundry",
                            "groupTypeForLabels": "amenities.unit-laundry",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 5900,
                            "date": "2023-05-10T20:33:14.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [
                        {
                            "from": "2023-06-17T13:00:00.000Z",
                            "to": "2023-06-17T14:00:00.000Z",
                            "__typename": "OpenHouse"
                        }
                    ],
                    "buildingClass": "condo",
                    "images": [
                        {
                            "imageUrl": "bulletins2/124755e87d4dbb25c981d5c25d4e6501.jpg",
                            "isFloorplan": true,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/a46d75bb20ef7f5b85494f3dfc0757d1.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/cd7b3ebc3da1e1645930580c8fd33b38.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/5d4c640859588809f6e5edc0df3c49ba.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/f06800e6977fc37db4c5deda8f88c0ba.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/75d75d8a4a34fb09367dd75d6a2b8970.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/0a50d464fa382babbac0ae02c22dce7b.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/cbe0d94490fdc717f4fe886130b0d224.png",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "rebny",
                    "originalId": "RPLU-33422430448",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Average crime rates",
                                    "tagLine": "CRIME",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "naturalLight",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "This apartment has limited sunlight",
                                    "tagLine": "",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "planning",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Near Historic District - less restrictions",
                                    "tagLine": "NEAR HISTORIC DISTRICT",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Lots of complaints about noise nearby",
                                    "tagLine": "NOISY AREA",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "livability",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Limited park access",
                                    "tagLine": "",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "prices",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Only 3 similar listings under $6.2K!",
                                    "tagLine": "PRICE OPPORTUNITY",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Dangerous intersection nearby",
                                    "tagLine": "ROAD SAFETY ISSUE",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-d3u8779iid0i",
                    "locationPoint": {
                        "lat": 40.68167495727539,
                        "lng": -73.94290924072266,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-12T00:38:25.168Z",
                    "addressDetails": {
                        "docId": "196-macon-street-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11216",
                        "streetName": "macon street",
                        "neighbourhood": "bedford stuyvesant",
                        "neighbourhoodDocId": "bedford-stuyvesant-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "196",
                        "unitNumber": "1E",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 56,
                    "address": "196 Macon Street, Brooklyn, New York",
                    "beds": 4,
                    "area": null,
                    "price": 4500,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Laundry in building",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.building-laundry",
                            "groupTypeForLabels": "amenities.building-laundry",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Building terrace",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.building-patio",
                            "groupTypeForLabels": "amenities.shared_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 4500,
                            "date": "2023-05-12T00:41:47.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": "co-op",
                    "images": [
                        {
                            "imageUrl": "bulletins2/a2e4a06753c7aeb5a1a8c64c49b56bdd.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/6fc70312ef35de2645c68699ce6067a2.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/bef293383a08fd7f33e5dcbe40f9bf58.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/dbe9d6f2cc4eb844d5b2541aa586ea5a.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/2e201bc7b50f390ff5788cdf2623c165.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/b0d819071be8eff96cf51a64c8ffa19a.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/6253f4ca99d4f6e83df5cce7db1c088e.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/76e31d53b0d033893c42aae691dad331.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/a38abc29567b499292613a4547984a16.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/6e4f6e0fac94041c6230b5ae380c8210.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/d24d2b557296b09aab89004ffe915aff.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/d74c6568a59a49edb3b53beb8efd1327.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/8f1ca419432947fc4ab92744c750d64b.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/a286b0297db17caf04d722ee75f889f0.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/a93f2c206161150f668bbe376ceaa492.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/9bf5f7ff45954dcfeb7a60e60be2caf0.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/7e8b251c48bf8bc429c402850812bceb.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/775ba8e6037838eed0fd1b5b6dbeaca5.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/b6060938c9eb40014fc5cbff3c5efb02.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/a9dd003a98602da91b139923141fb3cd.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/3ec0d9941afc804a2ba0afa81fc73d4d.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/d946a42cafc4be1c084cbfb846586e2d.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/df15b4b8aab178f1381a0e610bf3a98a.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/dae8de1c6697f3e2f9e2b1d0acd57136.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/f6bf5787c3769cb6debc00333e1cfc3c.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/250626a48c3a3648ceeb69c6c3457371.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "rebny",
                    "originalId": "RLMX-89330",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Slightly above average crime rate",
                                    "tagLine": "CRIME",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "planning",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Construction site next door",
                                    "tagLine": "CONSTRUCTION COMING",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "planning",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Near Historic District - less restrictions",
                                    "tagLine": "NEAR HISTORIC DISTRICT",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Lots of complaints about noise nearby",
                                    "tagLine": "NOISY AREA",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Dangerous intersection nearby",
                                    "tagLine": "ROAD SAFETY ISSUE",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-8usrdb1vd688",
                    "locationPoint": {
                        "lat": 40.711585998535156,
                        "lng": -73.94186401367188,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-13T04:24:07.263Z",
                    "addressDetails": {
                        "docId": "774-grand-street-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11206",
                        "streetName": "grand street",
                        "neighbourhood": "williamsburg",
                        "neighbourhoodDocId": "williamsburg-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "774",
                        "unitNumber": "4E",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 55,
                    "address": "774 Grand Street, Brooklyn, New York",
                    "beds": 2,
                    "area": null,
                    "price": 5575,
                    "pricesEstimations": {
                        "initialPrice": 5575,
                        "estimatedPrice": 5400,
                        "boundaries": {
                            "topBoundary": 5950,
                            "bottomBoundary": 4850,
                            "__typename": "PricesEstimationsBoundaries"
                        },
                        "__typename": "PricesEstimations"
                    },
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Washer/dryer",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-laundry",
                            "groupTypeForLabels": "amenities.unit-laundry",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 5575,
                            "date": "2023-05-13T04:28:03.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": "condo",
                    "images": [
                        {
                            "imageUrl": "bulletins2/4ad38f73043cca17be65bd5c1b3127d0.jpg",
                            "isFloorplan": true,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/2e4e77edd1a201bf45831291d403e804.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/12ea3325389b19ca8e2f717db68b3c19.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/0224399f8bbb0788452a208bf0bc397c.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/9fe300f208da2812460f151732beb8b3.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/44a39cc689bec515892b475dbeeba39b.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "rebny",
                    "originalId": "RPLU-5122471101",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Slightly above average crime rate",
                                    "tagLine": "CRIME",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Broken elevator reported",
                                    "tagLine": "ELEVATOR ISSUES",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "livability",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Good park access",
                                    "tagLine": "",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Dangerous intersection nearby",
                                    "tagLine": "ROAD SAFETY ISSUE",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-oc2p2d78k01e",
                    "locationPoint": {
                        "lat": 40.64342498779297,
                        "lng": -73.97534942626953,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-11T04:29:27.860Z",
                    "addressDetails": {
                        "docId": "503-beverly-road-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11218",
                        "streetName": "beverley road",
                        "neighbourhood": "kensington",
                        "neighbourhoodDocId": "kensington-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "503",
                        "unitNumber": "1B",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 57,
                    "address": "503 Beverley Road, Brooklyn, New York",
                    "beds": 2,
                    "area": null,
                    "price": 2800,
                    "pricesEstimations": {
                        "initialPrice": 2800,
                        "estimatedPrice": 3100,
                        "boundaries": {
                            "topBoundary": 3250,
                            "bottomBoundary": 2950,
                            "__typename": "PricesEstimationsBoundaries"
                        },
                        "__typename": "PricesEstimations"
                    },
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 2800,
                            "date": "2023-05-11T04:32:53.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": "rental unit",
                    "images": [
                        {
                            "imageUrl": "bulletins2/aa4f80a2c8eb05569dcff9db67194903.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/bf760585d3eed0c5e7272c0e758caff4.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/d86106c703a519ab3b19cbc230a846ab.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/4aa0be411dfc84486b5cefc552fc9bca.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/19a646b21849f895d04ab383cda78554.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/6b30949ac272110efeea39eaaa21a480.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/b65b3de15789aa33e51c806c229408e1.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/02bc125d2826f002cadc586d7864f886.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/245540ae0e4a597f78e4fcd659d7c0b8.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/6db955ab40e3eb1e2bd11c6d5b5ed810.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/572a038189a3a0d1f044c6182ea0717f.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/ed111ac694675cdcb38640e41e7cfd07.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/1703d26d2910eca9a42d2a813965e01c.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/6747bfbf7453aec71f8c5e87b18baa10.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/6ddfcc1d7cae587709500701ea470ffe.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/da2e39fbb16c6471775fe52171fd7fb5.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/178ce15aa48f9c6fb0025e5863a2b794.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/ff62f6dbfe8e2a8105445f3e3ed925b3.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/149c34e56208ebdd5a697ba88cf2a898.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/1f24d441e4bf436adb9150ea6081a8a7.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/983a775f70b76f8d7874a03da3bb72a8.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/0f86fd6b719c73b5ae0c9b3e2f0da23e.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/107dc2d768de2f4bbc6fb7547f851bd3.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/e1c3d0e02dd0150d8e66355254004102.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/671d11ae4c40d26dff1efce855c9b3fc.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "rebny",
                    "originalId": "RLMX-89318",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Below average crime rate",
                                    "tagLine": "CRIME",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "prices",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Price is 10% lower than similar listings!",
                                    "tagLine": "LOW PRICE",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "livability",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Limited park access",
                                    "tagLine": "",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-g2i2sttf59q0",
                    "locationPoint": {
                        "lat": 40.667938232421875,
                        "lng": -73.93698120117188,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-23T12:21:28.116Z",
                    "addressDetails": {
                        "docId": "1578-union-street-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11213",
                        "streetName": "union street",
                        "neighbourhood": "crown heights",
                        "neighbourhoodDocId": "crown-heights-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "1578",
                        "unitNumber": "3B",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": null,
                    "dealType": "unitRent",
                    "daysOnMarket": 45,
                    "address": "1578 Union Street, Brooklyn, New York",
                    "beds": 3,
                    "area": null,
                    "price": 4000,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Garden",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garden",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Patio",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.patio",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Balcony",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.balcony",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Roofdeck",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.roof-deck",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Terrace",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.terrace",
                            "groupTypeForLabels": "amenities.private_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Courtyard",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.courtyard",
                            "groupTypeForLabels": "amenities.shared_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "City views",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.city-view",
                            "groupTypeForLabels": "amenities.views",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Park views",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.park-view",
                            "groupTypeForLabels": "amenities.views",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Washer/dryer",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-laundry",
                            "groupTypeForLabels": "amenities.unit-laundry",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Doorman",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.doorman",
                            "groupTypeForLabels": "amenities.doorman",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Concierge",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.concierge",
                            "groupTypeForLabels": "amenities.concierge",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.fitness-room",
                            "groupTypeForLabels": "amenities.fitness-room",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Fireplace",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.fireplace",
                            "groupTypeForLabels": "amenities.fireplace",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Building garden",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.building-garden",
                            "groupTypeForLabels": "amenities.shared_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.health-club",
                            "groupTypeForLabels": "amenities.health-club",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Elevator",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.elevator",
                            "groupTypeForLabels": "amenities.elevator",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Air conditioner",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.air-conditioner",
                            "groupTypeForLabels": "amenities.air-conditioner",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Building terrace",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.building-patio",
                            "groupTypeForLabels": "amenities.shared_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Building terrace",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.building-terrace",
                            "groupTypeForLabels": "amenities.shared_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Bike storage",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.bike-storage",
                            "groupTypeForLabels": "amenities.bike-storage",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": null,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 4250,
                            "date": "2023-05-23T12:22:13.000Z",
                            "__typename": "EventUpdate"
                        },
                        {
                            "eventType": "priceDrop",
                            "price": 4000,
                            "date": "2023-06-21T12:21:56.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": "rental unit",
                    "images": [
                        {
                            "imageUrl": "bulletins2/6217ba9d6b332a7c94e4b826447c2a8c.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/071a9d8ac975d0199f3b96fd62063626.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/e46ab39e07be4282b1868b91faca11c5.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/b14897b982e702ef405277723ec36c81.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/c68fde408cc17f2aa2da87784f78c88d.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/a8b6b98dcfb5d710ccc4a2f2885337c7.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/7808289e8f30f5043e4ff1142e24e9c4.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "realtymx",
                    "originalId": "RealStreet_6733",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Average crime rates",
                                    "tagLine": "CRIME",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "livability",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Good park access",
                                    "tagLine": "",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "2 Open Violations in building",
                                    "tagLine": "BLDG VIOLATIONS",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-u8huhaukevap",
                    "locationPoint": {
                        "lat": 40.690948486328125,
                        "lng": -73.98236083984375,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-13T00:33:55.326Z",
                    "addressDetails": {
                        "docId": "55-fleet-street-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11201",
                        "streetName": "fleet street",
                        "neighbourhood": "downtown brooklyn",
                        "neighbourhoodDocId": "downtown-brooklyn-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "55",
                        "unitNumber": "16B",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 55,
                    "address": "55 Fleet Street, Brooklyn, New York",
                    "beds": 0,
                    "area": null,
                    "price": 4127,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Washer/dryer",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-laundry",
                            "groupTypeForLabels": "amenities.unit-laundry",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 4127,
                            "date": "2023-05-13T00:37:51.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": "condo",
                    "images": [
                        {
                            "imageUrl": "bulletins2/4cc272dee3ec0ce0e418129f8c9f9355.jpg",
                            "isFloorplan": true,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/b14669c9b4aaa82de659aaf868ef6364.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/e7a33f4422dd9c9ebb31eb3fb929e200.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/e44ab86d9226f17e93a1b6b78d9b65a1.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/b5c5d0478cfd50475f4bdc9fd184726d.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/72965a7f4116ddf825f4353f063cb8ba.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "rebny",
                    "originalId": "RPLU-5122469906",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Above average crime rate",
                                    "tagLine": "CRIME",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Building sits along truck route",
                                    "tagLine": "ON A TRUCK ROUTE",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "planning",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Construction site next door",
                                    "tagLine": "CONSTRUCTION COMING",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Lots of complaints about noise nearby",
                                    "tagLine": "NOISY AREA",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "prices",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Price is 15% higher than similar listings!",
                                    "tagLine": "HIGH PRICE",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "livability",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Limited park access",
                                    "tagLine": "",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Dangerous intersection nearby",
                                    "tagLine": "ROAD SAFETY ISSUE",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-24b6ugt5p2us",
                    "locationPoint": {
                        "lat": 40.684326171875,
                        "lng": -73.91656494140625,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-12T00:38:25.163Z",
                    "addressDetails": {
                        "docId": "741-mac-donough-street-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11233",
                        "streetName": "mac donough street",
                        "neighbourhood": "crown heights",
                        "neighbourhoodDocId": "crown-heights-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "741",
                        "unitNumber": "D2",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 56,
                    "address": "741 Mac Donough Street, Brooklyn, New York",
                    "beds": 3,
                    "area": 1269,
                    "price": 4000,
                    "pricesEstimations": {
                        "initialPrice": 4000,
                        "estimatedPrice": 3600,
                        "boundaries": {
                            "topBoundary": 4050,
                            "bottomBoundary": 3150,
                            "__typename": "PricesEstimationsBoundaries"
                        },
                        "__typename": "PricesEstimations"
                    },
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Washer/dryer",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-laundry",
                            "groupTypeForLabels": "amenities.unit-laundry",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Juliet-balcony",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.juliet-balcony",
                            "groupTypeForLabels": "amenities.juliet-balcony",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Building garden",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.building-garden",
                            "groupTypeForLabels": "amenities.shared_outdoor_space",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 4000,
                            "date": "2023-05-12T00:40:39.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [],
                    "buildingClass": "condo",
                    "images": [
                        {
                            "imageUrl": "bulletins2/b58ca455f7db02d76906c965cb6a9884.jpg",
                            "isFloorplan": true,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/7cd193264ec47b42ff94ff39e06c549e.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/221581fd0d22e1f1db4bad7293f3c7ce.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/29c5970bdc24de34d6e36b8e30c29027.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/5af36b6a90da9606416c2ae2ecda5860.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/4828dc71416de853ab2336f2e83be002.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/a636961f40af0bd76ba0b9abc731266e.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/79d5909a16aeccef6b98a6833147aef1.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/484cdb77a5c5b5961a11e7fc76e155f0.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "rebny",
                    "originalId": "OLRS-2036768",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Above average crime rate",
                                    "tagLine": "CRIME",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "naturalLight",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "This apartment has limited sunlight",
                                    "tagLine": "",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Lots of complaints about noise nearby",
                                    "tagLine": "NOISY AREA",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "prices",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "270 sq ft more than similar listings! Nice find!",
                                    "tagLine": "MORE SQ FT",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                },
                {
                    "id": "l-a38u1cagfonq",
                    "locationPoint": {
                        "lat": 40.67728042602539,
                        "lng": -73.90646362304688,
                        "__typename": "Point"
                    },
                    "firstTimeSeen": "2023-05-12T04:28:49.902Z",
                    "addressDetails": {
                        "docId": "1419-herkimer-street-brooklyn-new-york-ny",
                        "city": "new york",
                        "borough": "brooklyn",
                        "zipcode": "11233",
                        "streetName": "herkimer street",
                        "neighbourhood": "crown heights",
                        "neighbourhoodDocId": "crown-heights-neighborhood-brooklyn-new-york-ny",
                        "cityDocId": "new-york-ny",
                        "streetNumber": "1419",
                        "unitNumber": "GARDEN",
                        "district": "",
                        "__typename": "PoiAddress"
                    },
                    "providerListingStatus": "Active",
                    "dealType": "unitRent",
                    "daysOnMarket": 56,
                    "address": "1419 Herkimer Street, Brooklyn, New York",
                    "beds": 2,
                    "area": null,
                    "price": 4500,
                    "pricesEstimations": null,
                    "__typename": "Bulletin",
                    "lowMonthlies": false,
                    "listingDataFields": [
                        {
                            "meta": {
                                "text": "Pets allowed",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.unit-pets-allowed",
                            "groupTypeForLabels": "amenities.unit-pets-allowed",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Gym",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.gym",
                            "groupTypeForLabels": "amenities.gym",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Pool",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.pool",
                            "groupTypeForLabels": "amenities.pool",
                            "__typename": "ListingDataFieldItem"
                        },
                        {
                            "meta": {
                                "text": "Parking",
                                "__typename": "AmenityMetaData"
                            },
                            "type": "amenities.garage",
                            "groupTypeForLabels": "amenities.parking",
                            "__typename": "ListingDataFieldItem"
                        }
                    ],
                    "virtualTours": {
                        "hasVirtualTour": false,
                        "items": [],
                        "__typename": "VirtualTours"
                    },
                    "rentalBrokerFee": true,
                    "eventsHistory": [
                        {
                            "eventType": "new",
                            "price": 4500,
                            "date": "2023-05-12T04:32:38.000Z",
                            "__typename": "EventUpdate"
                        }
                    ],
                    "poc": {
                        "exclusivity": null,
                        "__typename": "AgentPoc"
                    },
                    "openHouses": [
                        {
                            "from": "2023-06-08T14:00:00.000Z",
                            "to": "2023-06-08T15:00:00.000Z",
                            "__typename": "OpenHouse"
                        }
                    ],
                    "buildingClass": "condo",
                    "images": [
                        {
                            "imageUrl": "bulletins2/4567575fea90af96147e4a86810e2bfa.jpg",
                            "isFloorplan": true,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/c80b066d8cbf467d006e3aa20fa9f366.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/aaf38aded5c234c104e24a1a183fe862.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/8cad92d21ea5e02db568f1abdcf0a022.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/abc8acb53f2f7b7e8d10b2014434007b.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/1f2e90dbf58adee26be7dceb901b52de.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/0b03f0ca08d63177059013e7fbc4a4b9.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/2f5c3c9d752801ece278c157399b9a7b.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/ebfa8a7dbad781202f33c9deb927f060.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        },
                        {
                            "imageUrl": "bulletins2/5a53bce1952c258c5a754757157f63fc.jpg",
                            "isFloorplan": false,
                            "__typename": "ImageItem"
                        }
                    ],
                    "commonCharges": null,
                    "monthlyTaxes": null,
                    "source": "rebny",
                    "originalId": "RPLU-5122463067",
                    "insights": {
                        "insights": [
                            {
                                "category": "safety",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Above average crime rate",
                                    "tagLine": "CRIME",
                                    "impactful": true,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            },
                            {
                                "category": "nuisances",
                                "tradeoff": {
                                    "insightPlace": null,
                                    "value": "Lots of complaints about noise nearby",
                                    "tagLine": "NOISY AREA",
                                    "impactful": false,
                                    "__typename": "Tradeoff"
                                },
                                "__typename": "Insight"
                            }
                        ],
                        "__typename": "Insights"
                    }
                }
            ],
            "__typename": "SearchBulletinResponse"
        }
    }
}"""
data = json.loads(localize_json_string)
print(type(data))
print(type(data['data']['searchResult']['poi']))

print(len([poi['id']for poi in data['data']['searchResult']['poi']]))

# Defining function to read in localize.city's search result json-pages

def json_to_dict(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

#Read json files with search results and covert to dict
filepaths = [
    '/Users/ligeaalexander/Desktop/Developer/Project-2/brooklyn_prospect_listing_result_page1.json',
    '/Users/ligeaalexander/Desktop/Developer/Project-2/brooklyn_prospect_listing_result_page2.json', 
    '/Users/ligeaalexander/Desktop/Developer/Project-2/brooklyn_prospect_listing_result_page3.json', 
    '/Users/ligeaalexander/Desktop/Developer/Project-2/brooklyn_prospect_listing_result_page4.json', 
    '/Users/ligeaalexander/Desktop/Developer/Project-2/brooklyn_prospect_listing_result_page5.json', 
    '/Users/ligeaalexander/Desktop/Developer/Project-2/brooklyn_prospect_listing_result_page6.json', 
    '/Users/ligeaalexander/Desktop/Developer/Project-2/brooklyn_prospect_listing_result_page7.json', 
    '/Users/ligeaalexander/Desktop/Developer/Project-2/brooklyn_prospect_listing_result_page8.json', 
    '/Users/ligeaalexander/Desktop/Developer/Project-2/brooklyn_prospect_listing_result_page9.json', 
    '/Users/ligeaalexander/Desktop/Developer/Project-2/brooklyn_prospect_listing_result_page10.json',
    '/Users/ligeaalexander/Desktop/Developer/Project-2/brooklyn_prospect_listing_result_page11.json', 
    '/Users/ligeaalexander/Desktop/Developer/Project-2/brooklyn_prospect_listing_result_page12.json', 
    '/Users/ligeaalexander/Desktop/Developer/Project-2/brooklyn_prospect_listing_result_page13.json']

dictionaries = [json_to_dict(filepath) for filepath in filepaths]
print(type(dictionaries))
print(type(dictionaries[0]))
print(dictionaries[0].keys())

# for dict in dictionaries[0]:
#     print(dict['data']['searchResult'])
#     # for id in dict['data']['searchResult']['poi'][0]:
#     #     print(id)

# print(dictionaries[0]['data']['searchResult'].keys())
# print(dictionaries[0]['data']['searchResult']['poi'][0].keys())
print(dictionaries[0]['data']['searchResult']['poi'][0]['insights']['insights'])

