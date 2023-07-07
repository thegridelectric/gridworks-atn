""" DNode (Dijkstra Node) Definition """
from abc import ABC
from typing import Optional


SIG_FIGS_FOR_OUTPUT = 6


class DNode(ABC):
    SIG_FIGS_FOR_OUTPUT = 6

    def __init__(
        self,
        ts_idx: int,
        store_idx: int,
        local_benefit: float = 0,
    ):
        self.ts_idx = ts_idx
        """
        The time slice index of the node, starting with ts_idx = 0 for the earliest time slice.
        """

        self.store_idx = store_idx
        """
        The fullness of the store.
        """

        self.local_benefit = local_benefit
        """
        A "benefit function" that can be associated to nodes. This can be used, for example, to
        create penalty functions if set to negative numbers. Alternatively, it can always be
        set as a positive number in order to capture the 'good' provided by the device being
        in that state.
        """

        self.path_benefit: Optional[float] = None
        """
        The benefit associated to the optimal path from this point to the final time slice,
        where optimization means maximum benefit.
        """

        self.best_next_idx: Optional[int] = None
        """
        The store index of the next best step along the optimal path, from this node.
        """

        self.path_edge_cost_only: Optional[float] = None
        """
        The sum of the edge costs of the optimal path - that is, removing the local benefit from
        nodes.
        """

    @property
    def path_cost(self) -> Optional[float]:
        """
        The cost of the optimal path from this point to the final time slice,
        where optimization means minimum cost.
        """
        if self.path_benefit is None:
            return None
        return -self.path_benefit

    def __repr__(self) -> str:
        if self.local_benefit:
            local_benefit = round(self.local_benefit, self.SIG_FIGS_FOR_OUTPUT)
        else:
            local_benefit = None
        if self.path_benefit:
            path_benefit = round(self.path_benefit, self.SIG_FIGS_FOR_OUTPUT)
        else:
            path_benefit = None
        if self.path_edge_cost_only:
            path_edge_cost_only = round(
                self.path_edge_cost_only, self.SIG_FIGS_FOR_OUTPUT
            )
        else:
            path_edge_cost_only = None
        return (
            f"DNode => TsIdx: {self.ts_idx}, StoreIdx: {self.store_idx}, BestNextIdx: {self.best_next_idx}, "
            f"LocalBenefit: {local_benefit}, PathBenefit: {path_benefit}, PathEdgeCostOnly: {path_edge_cost_only}"
        )
