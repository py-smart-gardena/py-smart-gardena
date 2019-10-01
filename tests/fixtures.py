location_fixture = {
    "attributes": {"name": "My Garden"},
    "id": "753aecac-4c46-470e-aa96-d92436f11e77",
    "relationships": {
        "devices": {
            "data": [
                {"id": "28c26146-d4c1-42d7-964a-89f5237550ce", "type": "DEVICE"},
                {"id": "7859acad-b23e-4abf-bec6-62c1453fc34c", "type": "DEVICE"},
                {"id": "7859acbd-b23e-dabf-bec6-62c1453fc44c", "type": "DEVICE"},
                {"id": "a134596e-6127-4020-aaa5-b6d2f24d0d03", "type": "DEVICE"},
                {"id": "d6459669-8171-488c-ab8e-bcf3a06a58bf", "type": "DEVICE"},
            ]
        }
    },
    "type": "LOCATION",
}

mower_fixture = {
    "COMMON": [
        {
            "attributes": {
                "batteryLevel": {
                    "timestamp": "2019-09-29T08:19:47.715+0000",
                    "value": 100,
                },
                "batteryState": {
                    "timestamp": "2019-09-29T07:43:44.115+0000",
                    "value": "OK",
                },
                "modelType": {"value": "GARDENA " "smart " "Mower"},
                "name": {"value": "SILENO"},
                "rfLinkLevel": {
                    "timestamp": "2019-09-29T07:47:47.776+0000",
                    "value": 50,
                },
                "rfLinkState": {"value": "ONLINE"},
                "serial": {"value": "00003676"},
            },
            "id": "7859acbd-b23e-dabf-bec6-62c1453fc44c",
            "relationships": {
                "device": {
                    "data": {
                        "id": "7859acbd-b23e-dabf-bec6-62c1453fc44c",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "COMMON",
        }
    ],
    "DEVICE": [
        {
            "id": "7859acbd-b23e-dabf-bec6-62c1453fc44c",
            "relationships": {
                "location": {
                    "data": {
                        "id": "753aecac-4c46-470e-aa96-d92436f11e77",
                        "type": "LOCATION",
                    }
                },
                "services": {
                    "data": [
                        {"id": "7859acbd-b23e-dabf-bec6-62c1453fc44c", "type": "MOWER"},
                        {
                            "id": "7859acbd-b23e-dabf-bec6-62c1453fc44c",
                            "type": "COMMON",
                        },
                    ]
                },
            },
            "type": "DEVICE",
        }
    ],
    "MOWER": [
        {
            "attributes": {
                "activity": {
                    "timestamp": "2019-09-29T07:43:44.115+0000",
                    "value": "PARKED_PARK_SELECTED",
                },
                "operatingHours": {"value": 40},
                "state": {"timestamp": "2019-09-29T07:43:44.115+0000", "value": "OK"},
            },
            "id": "7859acbd-b23e-dabf-bec6-62c1453fc44c",
            "relationships": {
                "device": {
                    "data": {
                        "id": "7859acbd-b23e-dabf-bec6-62c1453fc44c",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "MOWER",
        }
    ],
}

sensor_fixture = {
    "COMMON": [
        {
            "attributes": {
                "batteryLevel": {
                    "timestamp": "2019-09-28T22:54:29.179+0000",
                    "value": 93,
                },
                "batteryState": {
                    "timestamp": "2019-09-21T08:49:53.225+0000",
                    "value": "OK",
                },
                "modelType": {"value": "GARDENA " "smart " "Sensor"},
                "name": {"value": "Sensor"},
                "rfLinkLevel": {
                    "timestamp": "2019-09-29T10:56:10.257+0000",
                    "value": 70,
                },
                "rfLinkState": {"value": "ONLINE"},
                "serial": {"value": "00028462"},
            },
            "id": "a134596e-6127-4020-aaa5-b6d2f24d0d03",
            "relationships": {
                "device": {
                    "data": {
                        "id": "a134596e-6127-4020-aaa5-b6d2f24d0d03",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "COMMON",
        }
    ],
    "DEVICE": [
        {
            "id": "a134596e-6127-4020-aaa5-b6d2f24d0d03",
            "relationships": {
                "location": {
                    "data": {
                        "id": "753aecac-4c46-470e-aa96-d92436f11e77",
                        "type": "LOCATION",
                    }
                },
                "services": {
                    "data": [
                        {
                            "id": "a134596e-6127-4020-aaa5-b6d2f24d0d03",
                            "type": "SENSOR",
                        },
                        {
                            "id": "a134596e-6127-4020-aaa5-b6d2f24d0d03",
                            "type": "COMMON",
                        },
                    ]
                },
            },
            "type": "DEVICE",
        }
    ],
    "SENSOR": [
        {
            "attributes": {
                "ambientTemperature": {
                    "timestamp": "2019-09-29T10:56:10.122+0000",
                    "value": 21,
                },
                "lightIntensity": {
                    "timestamp": "2019-09-29T10:56:10.215+0000",
                    "value": 15,
                },
                "soilHumidity": {
                    "timestamp": "2019-09-29T10:03:27.485+0000",
                    "value": 0,
                },
                "soilTemperature": {
                    "timestamp": "2019-09-29T10:02:18.119+0000",
                    "value": 22,
                },
            },
            "id": "a134596e-6127-4020-aaa5-b6d2f24d0d03",
            "relationships": {
                "device": {
                    "data": {
                        "id": "a134596e-6127-4020-aaa5-b6d2f24d0d03",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "SENSOR",
        }
    ],
}

smart_irrigation_fixture = {
    "COMMON": [
        {
            "attributes": {
                "batteryState": {"value": "NO_BATTERY"},
                "modelType": {"value": "GARDENA " "smart " "Irrigation " "Control"},
                "name": {"value": "Irrigation " "Control"},
                "rfLinkLevel": {
                    "timestamp": "2019-02-04T08:42:55.589+0000",
                    "value": 100,
                },
                "rfLinkState": {"value": "OFFLINE"},
                "serial": {"value": "00001834"},
            },
            "id": "28c26146-d4c1-42d7-964a-89f5237550ce",
            "relationships": {
                "device": {
                    "data": {
                        "id": "28c26146-d4c1-42d7-964a-89f5237550ce",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "COMMON",
        }
    ],
    "DEVICE": [
        {
            "id": "28c26146-d4c1-42d7-964a-89f5237550ce",
            "relationships": {
                "location": {
                    "data": {
                        "id": "753aecac-4c46-470e-aa96-d92436f11e77",
                        "type": "LOCATION",
                    }
                },
                "services": {
                    "data": [
                        {
                            "id": "28c26146-d4c1-42d7-964a-89f5237550ce",
                            "type": "VALVE_SET",
                        },
                        {
                            "id": "28c26146-d4c1-42d7-964a-89f5237550ce:1",
                            "type": "VALVE",
                        },
                        {
                            "id": "28c26146-d4c1-42d7-964a-89f5237550ce:2",
                            "type": "VALVE",
                        },
                        {
                            "id": "28c26146-d4c1-42d7-964a-89f5237550ce:3",
                            "type": "VALVE",
                        },
                        {
                            "id": "28c26146-d4c1-42d7-964a-89f5237550ce:4",
                            "type": "VALVE",
                        },
                        {
                            "id": "28c26146-d4c1-42d7-964a-89f5237550ce:5",
                            "type": "VALVE",
                        },
                        {
                            "id": "28c26146-d4c1-42d7-964a-89f5237550ce:6",
                            "type": "VALVE",
                        },
                        {
                            "id": "28c26146-d4c1-42d7-964a-89f5237550ce",
                            "type": "COMMON",
                        },
                    ]
                },
            },
            "type": "DEVICE",
        }
    ],
    "VALVE": [
        {
            "attributes": {
                "activity": {
                    "timestamp": "2019-02-01T18:54:06.527+0000",
                    "value": "CLOSED",
                },
                "lastErrorCode": {
                    "timestamp": "2019-02-01T18:54:06.700+0000",
                    "value": "NO_MESSAGE",
                },
                "name": {"value": "Clapet 1"},
                "state": {
                    "timestamp": "2019-02-01T18:54:12.719+0000",
                    "value": "UNAVAILABLE",
                },
            },
            "id": "28c26146-d4c1-42d7-964a-89f5237550ce:1",
            "relationships": {
                "device": {
                    "data": {
                        "id": "28c26146-d4c1-42d7-964a-89f5237550ce",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "VALVE",
        },
        {
            "attributes": {
                "activity": {
                    "timestamp": "2019-02-01T18:54:06.543+0000",
                    "value": "CLOSED",
                },
                "lastErrorCode": {
                    "timestamp": "2019-02-01T18:54:06.712+0000",
                    "value": "NO_MESSAGE",
                },
                "name": {"value": "Valve " "2"},
                "state": {
                    "timestamp": "2019-02-01T18:54:12.719+0000",
                    "value": "UNAVAILABLE",
                },
            },
            "id": "28c26146-d4c1-42d7-964a-89f5237550ce:2",
            "relationships": {
                "device": {
                    "data": {
                        "id": "28c26146-d4c1-42d7-964a-89f5237550ce",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "VALVE",
        },
        {
            "attributes": {
                "activity": {
                    "timestamp": "2019-02-01T18:54:06.559+0000",
                    "value": "CLOSED",
                },
                "lastErrorCode": {
                    "timestamp": "2019-02-01T18:54:06.722+0000",
                    "value": "NO_MESSAGE",
                },
                "name": {"value": "Valve " "3"},
                "state": {
                    "timestamp": "2019-02-01T18:54:12.719+0000",
                    "value": "UNAVAILABLE",
                },
            },
            "id": "28c26146-d4c1-42d7-964a-89f5237550ce:3",
            "relationships": {
                "device": {
                    "data": {
                        "id": "28c26146-d4c1-42d7-964a-89f5237550ce",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "VALVE",
        },
        {
            "attributes": {
                "activity": {
                    "timestamp": "2019-02-01T18:54:06.577+0000",
                    "value": "CLOSED",
                },
                "lastErrorCode": {
                    "timestamp": "2019-02-01T18:54:06.732+0000",
                    "value": "NO_MESSAGE",
                },
                "name": {"value": "Valve " "4"},
                "state": {
                    "timestamp": "2019-02-01T18:54:12.719+0000",
                    "value": "UNAVAILABLE",
                },
            },
            "id": "28c26146-d4c1-42d7-964a-89f5237550ce:4",
            "relationships": {
                "device": {
                    "data": {
                        "id": "28c26146-d4c1-42d7-964a-89f5237550ce",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "VALVE",
        },
        {
            "attributes": {
                "activity": {
                    "timestamp": "2019-02-01T18:54:06.593+0000",
                    "value": "CLOSED",
                },
                "lastErrorCode": {
                    "timestamp": "2019-02-01T18:54:06.741+0000",
                    "value": "NO_MESSAGE",
                },
                "name": {"value": "Valve " "5"},
                "state": {
                    "timestamp": "2019-02-01T18:54:12.719+0000",
                    "value": "UNAVAILABLE",
                },
            },
            "id": "28c26146-d4c1-42d7-964a-89f5237550ce:5",
            "relationships": {
                "device": {
                    "data": {
                        "id": "28c26146-d4c1-42d7-964a-89f5237550ce",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "VALVE",
        },
        {
            "attributes": {
                "activity": {
                    "timestamp": "2019-02-01T18:54:06.610+0000",
                    "value": "CLOSED",
                },
                "lastErrorCode": {
                    "timestamp": "2019-02-01T18:54:06.806+0000",
                    "value": "NO_MESSAGE",
                },
                "name": {"value": "Valve " "6"},
                "state": {
                    "timestamp": "2019-02-01T18:54:12.719+0000",
                    "value": "UNAVAILABLE",
                },
            },
            "id": "28c26146-d4c1-42d7-964a-89f5237550ce:6",
            "relationships": {
                "device": {
                    "data": {
                        "id": "28c26146-d4c1-42d7-964a-89f5237550ce",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "VALVE",
        },
    ],
    "VALVE_SET": [
        {
            "attributes": {
                "lastErrorCode": {
                    "timestamp": "2019-02-01T18:54:06.674+0000",
                    "value": "NO_MESSAGE",
                },
                "state": {"timestamp": "2019-02-01T18:54:06.674+0000", "value": "OK"},
            },
            "id": "28c26146-d4c1-42d7-964a-89f5237550ce",
            "relationships": {
                "device": {
                    "data": {
                        "id": "28c26146-d4c1-42d7-964a-89f5237550ce",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "VALVE_SET",
        }
    ],
}

water_control_fixture = {
    "COMMON": [
        {
            "attributes": {
                "batteryLevel": {
                    "timestamp": "2019-09-29T10:52:27.307+0000",
                    "value": 99,
                },
                "batteryState": {
                    "timestamp": "2019-09-29T10:52:27.258+0000",
                    "value": "OK",
                },
                "modelType": {"value": "GARDENA " "smart " "Water " "Control"},
                "name": {"value": "Water " "Control"},
                "rfLinkLevel": {
                    "timestamp": "2019-09-29T10:52:27.345+0000",
                    "value": 70,
                },
                "rfLinkState": {"value": "ONLINE"},
                "serial": {"value": "00019796"},
            },
            "id": "d6459669-8171-488c-ab8e-bcf3a06a58bf",
            "relationships": {
                "device": {
                    "data": {
                        "id": "d6459669-8171-488c-ab8e-bcf3a06a58bf",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "COMMON",
        }
    ],
    "DEVICE": [
        {
            "id": "d6459669-8171-488c-ab8e-bcf3a06a58bf",
            "relationships": {
                "location": {
                    "data": {
                        "id": "753aecac-4c46-470e-aa96-d92436f11e77",
                        "type": "LOCATION",
                    }
                },
                "services": {
                    "data": [
                        {
                            "id": "d6459669-8171-488c-ab8e-bcf3a06a58bf:wc",
                            "type": "VALVE_SET",
                        },
                        {"id": "d6459669-8171-488c-ab8e-bcf3a06a58bf", "type": "VALVE"},
                        {
                            "id": "d6459669-8171-488c-ab8e-bcf3a06a58bf",
                            "type": "COMMON",
                        },
                    ]
                },
            },
            "type": "DEVICE",
        }
    ],
    "VALVE": [
        {
            "attributes": {
                "activity": {
                    "timestamp": "2019-09-21T08:38:08.890+0000",
                    "value": "CLOSED",
                },
                "name": {"value": "Water " "Control"},
                "state": {"value": "OK"},
            },
            "id": "d6459669-8171-488c-ab8e-bcf3a06a58bf",
            "relationships": {
                "device": {
                    "data": {
                        "id": "d6459669-8171-488c-ab8e-bcf3a06a58bf",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "VALVE",
        }
    ],
    "VALVE_SET": [
        {
            "attributes": {},
            "id": "d6459669-8171-488c-ab8e-bcf3a06a58bf:wc",
            "relationships": {
                "device": {
                    "data": {
                        "id": "d6459669-8171-488c-ab8e-bcf3a06a58bf",
                        "type": "DEVICE",
                    }
                }
            },
            "type": "VALVE_SET",
        }
    ],
}
