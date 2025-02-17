# third party
import gevent

# relative
from .....logger import critical
from ....common.uid import UID
from ....store.storeable_object import StorableObject
from ...abstract.node import AbstractNode


def retrieve_object(
    node: AbstractNode, id_at_location: UID, path: str
) -> StorableObject:
    # A hard time limit is set on celery worker which prevents infinite execution.
    ctr = 0
    while True:
        store_obj = node.store.get_object(key=id_at_location)
        if store_obj is None:
            if ctr % 200 == 0:
                critical(
                    f"execute_action on {path} failed due to missing object"
                    + f" at: {id_at_location}"
                )
            # Implicit context switch between greenlets.
            gevent.sleep(0)
            ctr += 1
        else:
            return store_obj


def beaver_retrieve_object(
    node: AbstractNode, id_at_location: UID, nr_parties: int
) -> StorableObject:
    # A hard time limit is set on celery worker which prevents infinite execution.
    ctr = 0
    while True:
        store_obj = node.store.get_object(key=id_at_location)
        if store_obj is None or len(store_obj.data) != nr_parties:
            if ctr % 200 == 0:
                critical(
                    f"Beaver Retrieval failed for {nr_parties} parties due to missing object"
                    + f" at: {id_at_location} values: {store_obj}"
                )
            # Implicit context switch between greenlets.
            gevent.sleep(0)
            ctr += 1
        else:
            return store_obj
