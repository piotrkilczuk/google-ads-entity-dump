from __future__ import annotations

import dataclasses
import enum
from typing import Type, List

import proto


__all__ = ("Arc", "ArcType", "Graph", "Node", "symmetric_one_to_many", "symmetric_many_to_one", "symmetric_one_to_one")


# @TODO: Maybe one day this won't be required?
class Graph:
    nodes: List[Node] = dataclasses.field(default_factory=list)


@dataclasses.dataclass(repr=False)
class Node:
    ads_api_resource: Type[proto.Message]
    graph: Graph

    # @TODO: Could this be sets? If so, then how to make Arc hashable?
    outgoing_arcs: List[Arc] = dataclasses.field(default_factory=list)
    incoming_arcs: List[Arc] = dataclasses.field(default_factory=list)

    def __str__(self):
        return self.ads_api_resource.__name__

    def __repr__(self):
        return str(self)


class ArcType(enum.Enum):
    ONE_TO_MANY = "ONE_TO_MANY"
    MANY_TO_ONE = "MANY_TO_ONE"
    ONE_TO_ONE = "ONE_TO_ONE"


@dataclasses.dataclass(repr=False)
class Arc:
    type: ArcType
    lhs: Node
    rhs: Node

    def __post_init__(self):
        self.lhs.outgoing_arcs.append(self)
        self.rhs.incoming_arcs.append(self)

    def __str__(self):
        return f"<{self.type.name} from {self.lhs} to {self.rhs}>"

    def __repr__(self):
        return str(self)


def symmetric_many_to_one(many: Node, one: Node):
    Arc(ArcType.MANY_TO_ONE, many, one)
    Arc(ArcType.ONE_TO_MANY, one, many)


def symmetric_one_to_many(one: Node, many: Node):
    Arc(ArcType.ONE_TO_MANY, one, many)
    Arc(ArcType.MANY_TO_ONE, many, one)


def symmetric_one_to_one(first: Node, other: Node):
    Arc(ArcType.ONE_TO_ONE, first, other)
    Arc(ArcType.ONE_TO_ONE, other, first)
