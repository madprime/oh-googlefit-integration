import json

import datauploader.helpers


def test_should_leave_as_is_for_error():
    error = {'error': 'Christmas is going to the dogs'}
    # https://www.youtube.com/watch?v=lqUKbP_9lNo
    res = datauploader.helpers.remove_empty_buckets(error)
    assert res == error


def test_should_remove_empty_buckets():
    uncompressed_json = json.load(open('./datauploader/tests/sample_source.json'))

    compressed_json = datauploader.helpers.remove_empty_buckets(uncompressed_json)
    expected = {
                   "bucket": [

               {
                   "startTimeMillis": "1544011773862",
                   "endTimeMillis": "1544015373862",
                   "dataset": [
                       {
                           "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:aggregated",
                           "point": [
                               {
                                   "startTimeNanos": "1544013416678766386",
                                   "endTimeNanos": "1544013878080728183",
                                   "dataTypeName": "com.google.step_count.delta",
                                   "originDataSourceId": "raw:com.google.step_count.cumulative:HUAWEI:SLA-L22:95420828dc10aa6a:Step Counter",
                                   "value": [
                                       {
                                           "intVal": 50,
                                           "mapVal": []
                                       }
                                   ]
                               }
                           ]
                       }
                   ]
               },
               {
                   "startTimeMillis": "1544015373862",
                   "endTimeMillis": "1544018973862",
                   "dataset": [
                       {
                           "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:aggregated",
                           "point": [
                               {
                                   "startTimeNanos": "1544015643816231462",
                                   "endTimeNanos": "1544018973862000000",
                                   "dataTypeName": "com.google.step_count.delta",
                                   "originDataSourceId": "raw:com.google.step_count.cumulative:HUAWEI:SLA-L22:95420828dc10aa6a:Step Counter",
                                   "value": [
                                       {
                                           "intVal": 123,
                                           "mapVal": []
                                       }
                                   ]
                               }
                           ]
                       }
                   ]
               },
               {
                   "startTimeMillis": "1544018973862",
                   "endTimeMillis": "1544022573862",
                   "dataset": [
                       {
                           "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:aggregated",
                           "point": [
                               {
                                   "startTimeNanos": "1544018973862000000",
                                   "endTimeNanos": "1544019186782506668",
                                   "dataTypeName": "com.google.step_count.delta",
                                   "originDataSourceId": "raw:com.google.step_count.cumulative:HUAWEI:SLA-L22:95420828dc10aa6a:Step Counter",
                                   "value": [
                                       {
                                           "intVal": 14,
                                           "mapVal": []
                                       }
                                   ]
                               }
                           ]
                       }
                   ]
               },
               {
                   "startTimeMillis": "1544022573862",
                   "endTimeMillis": "1544026173862",
                   "dataset": [
                       {
                           "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:aggregated",
                           "point": [
                               {
                                   "startTimeNanos": "1544023895246260693",
                                   "endTimeNanos": "1544025318953550049",
                                   "dataTypeName": "com.google.step_count.delta",
                                   "originDataSourceId": "raw:com.google.step_count.cumulative:HUAWEI:SLA-L22:95420828dc10aa6a:Step Counter",
                                   "value": [
                                       {
                                           "intVal": 9,
                                           "mapVal": []
                                       }
                                   ]
                               }
                           ]
                       }
                   ]
               },
               {
                   "startTimeMillis": "1544026173862",
                   "endTimeMillis": "1544029773862",
                   "dataset": [
                       {
                           "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:aggregated",
                           "point": [
                               {
                                   "startTimeNanos": "1544027331000651666",
                                   "endTimeNanos": "1544029446672656127",
                                   "dataTypeName": "com.google.step_count.delta",
                                   "originDataSourceId": "raw:com.google.step_count.cumulative:HUAWEI:SLA-L22:95420828dc10aa6a:Step Counter",
                                   "value": [
                                       {
                                           "intVal": 35,
                                           "mapVal": []
                                       }
                                   ]
                               }
                           ]
                       }
                   ]
               },
               {
                   "startTimeMillis": "1544029773862",
                   "endTimeMillis": "1544033373862",
                   "dataset": [
                       {
                           "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:aggregated",
                           "point": [
                               {
                                   "startTimeNanos": "1544030996590841223",
                                   "endTimeNanos": "1544033373862000000",
                                   "dataTypeName": "com.google.step_count.delta",
                                   "originDataSourceId": "raw:com.google.step_count.cumulative:HUAWEI:SLA-L22:95420828dc10aa6a:Step Counter",
                                   "value": [
                                       {
                                           "intVal": 1687,
                                           "mapVal": []
                                       }
                                   ]
                               }
                           ]
                       }
                   ]
               },
               {
                   "startTimeMillis": "1544033373862",
                   "endTimeMillis": "1544036973862",
                   "dataset": [
                       {
                           "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:aggregated",
                           "point": [
                               {
                                   "startTimeNanos": "1544033373862000000",
                                   "endTimeNanos": "1544036761639091676",
                                   "dataTypeName": "com.google.step_count.delta",
                                   "originDataSourceId": "raw:com.google.step_count.cumulative:HUAWEI:SLA-L22:95420828dc10aa6a:Step Counter",
                                   "value": [
                                       {
                                           "intVal": 1139,
                                           "mapVal": []
                                       }
                                   ]
                               }
                           ]
                       }
                   ]
               },
               {
                   "startTimeMillis": "1544036973862",
                   "endTimeMillis": "1544040573862",
                   "dataset": [
                       {
                           "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:aggregated",
                           "point": [
                               {
                                   "startTimeNanos": "1544037380652733063",
                                   "endTimeNanos": "1544040573862000000",
                                   "dataTypeName": "com.google.step_count.delta",
                                   "originDataSourceId": "raw:com.google.step_count.cumulative:HUAWEI:SLA-L22:95420828dc10aa6a:Step Counter",
                                   "value": [
                                       {
                                           "intVal": 2058,
                                           "mapVal": []
                                       }
                                   ]
                               }
                           ]
                       }
                   ]
               },
               {
                   "startTimeMillis": "1544040573862",
                   "endTimeMillis": "1544044173862",
                   "dataset": [
                       {
                           "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:aggregated",
                           "point": [
                               {
                                   "startTimeNanos": "1544040573862000000",
                                   "endTimeNanos": "1544042208069133417",
                                   "dataTypeName": "com.google.step_count.delta",
                                   "originDataSourceId": "raw:com.google.step_count.cumulative:HUAWEI:SLA-L22:95420828dc10aa6a:Step Counter",
                                   "value": [
                                       {
                                           "intVal": 876,
                                           "mapVal": []
                                       }
                                   ]
                               }
                           ]
                       }
                   ]
               },
               {
                   "startTimeMillis": "1544044173862",
                   "endTimeMillis": "1544047773862",
                   "dataset": [
                       {
                           "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:aggregated",
                           "point": [
                               {
                                   "startTimeNanos": "1544044405479408310",
                                   "endTimeNanos": "1544047385830341054",
                                   "dataTypeName": "com.google.step_count.delta",
                                   "originDataSourceId": "raw:com.google.step_count.cumulative:HUAWEI:SLA-L22:95420828dc10aa6a:Step Counter",
                                   "value": [
                                       {
                                           "intVal": 2,
                                           "mapVal": []
                                       }
                                   ]
                               }
                           ]
                       }
                   ]
               },
               {
                   "startTimeMillis": "1544047773862",
                   "endTimeMillis": "1544051373862",
                   "dataset": [
                       {
                           "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:aggregated",
                           "point": [
                               {
                                   "startTimeNanos": "1544047796156897154",
                                   "endTimeNanos": "1544049802298870670",
                                   "dataTypeName": "com.google.step_count.delta",
                                   "originDataSourceId": "raw:com.google.step_count.cumulative:HUAWEI:SLA-L22:95420828dc10aa6a:Step Counter",
                                   "value": [
                                       {
                                           "intVal": 15,
                                           "mapVal": []
                                       }
                                   ]
                               }
                           ]
                       }
                   ]
               },
               {
                   "startTimeMillis": "1544051373862",
                   "endTimeMillis": "1544054973862",
                   "dataset": [
                       {
                           "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:aggregated",
                           "point": [
                               {
                                   "startTimeNanos": "1544053479653601079",
                                   "endTimeNanos": "1544053539653601079",
                                   "dataTypeName": "com.google.step_count.delta",
                                   "originDataSourceId": "raw:com.google.step_count.cumulative:HUAWEI:SLA-L22:95420828dc10aa6a:Step Counter",
                                   "value": [
                                       {
                                           "intVal": 1,
                                           "mapVal": []
                                       }
                                   ]
                               }
                           ]
                       }
                   ]
               },

    ]
    }

    assert compressed_json == expected
