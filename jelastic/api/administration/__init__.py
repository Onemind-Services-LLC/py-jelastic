from typing import Literal

from ..abstract import ClientAbstract

__all__ = ["Administration"]

MODE = Literal["STRONG", "MODERATE", "WEAK"]


class Administration(ClientAbstract):
    _endpoint1 = "administration"

    @property
    def Analytics(self) -> "_Analytics":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.administration.Analytics

        Ref: https://docs.jelastic.com/api/private/#!/api/administration.Analytics
        """
        return _Analytics(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )

    @property
    def Subscription(self) -> "_Subscription":
        """
        >>> from jelastic import Jelastic
        >>> jelastic = Jelastic('https://jca.xapp.cloudmydc.com', token='d6f4e314a5b5fefd164995169f28ae32d987704f')
        >>> jelastic.administration.Subscription

        Ref: https://docs.jelastic.com/api/private/#!/api/administration.Subscription
        """
        return _Subscription(
            session=self._session,
            token=self._token,
            debug=self._debug,
        )


class _Analytics(Administration):
    _endpoint2 = "analytics"

    def GetNodesAffinitySuggestion(
        self,
        target_app_ids: list[str] = None,
        node_groups: list[str] = None,
        uids: list[int] = None,
        thread_count: int = None,
    ):
        """
        A list of environments with one node in every layer where distribution can be optimized

        :param target_app_ids: list of the exact environments that should be analyzed
        :param node_groups: list of the node group IDs that should be analyzed
        :param uids: list of the user IDs that should be analyzed
        :param thread_count: a number of threads for container distribution analysis
        """
        return self._get(
            "GetNodesAffinitySuggestion",
            params={
                "targetAppIds": target_app_ids,
                "nodeGroups": node_groups,
                "uids": uids,
                "threadCount": thread_count,
            },
            delimiter=",",
        )

    def GetNodesAntiAffinitySuggestion(
        self,
        target_app_ids: list[str] = None,
        mode: MODE = None,
        node_groups: list[str] = None,
        uids: list[int] = None,
        thread_count: int = None,
    ):
        """
        A list of environments with non-optimal container distribution with optimization suggestions

        :param target_app_ids: list of the exact environments that should be analyzed
        :param mode: a mode of the anti-affinity analysis
        :param node_groups: list of the node group IDs that should be analyzed
        :param uids: list of the user IDs that should be analyzed
        :param thread_count: a number of threads for container distribution analysis
        """
        return self._get(
            "GetNodesAntiAffinitySuggestion",
            params={
                "targetAppIds": target_app_ids,
                "mode": mode,
                "nodeGroups": node_groups,
                "uids": uids,
                "threadCount": thread_count,
            },
            delimiter=",",
        )


class _Subscription(Administration):
    """
    Ref: https://docs.jelastic.com/api/private/#!/api/administration.Subscription
    """

    _endpoint2 = "subscription"

    def AddCategory(
        self,
        category: dict,
        reseller_id: list[int] = None,
    ):
        """
        :param category: JSON representation of an object (subscription Category) that should be created
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "AddCategory",
            params={
                "category": category,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def AddProduct(
        self,
        product: dict = None,
        reseller_id: list[int] = None,
    ):
        """
        :param category: JSON representation of an object (subscription Product) that should be created.
        :param product: unique identifier of the target reseller platform.
        """
        return self._get(
            "AddProduct",
            params={
                "product": product,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def AddServicePlan(
        self,
        service_plan: dict,
        reseller_id: list[int] = None,
        expand_fields: list[str] = None,
    ):
        """
        :param service_plan: JSON representation of an object (subscription Service Plan) that should be created.
        :param reseller_id: unique identifier of the target reseller platform.
        :param expand_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        """
        return self._get(
            "AddServicePlan",
            params={
                "servicePlan": service_plan,
                "resellerId": reseller_id,
                "expandFields": expand_fields,
            },
            delimiter=",",
        )

    def AddSubscriptionItemResource(
        self,
        subscription_id: int,
        item_id: int,
        item_resource_id: int,
        resources: dict,
    ):
        """

        :param subscription_id: unique identifier of the target subscription.
        :param item_id: unique identifier of the target subscription item.
        :param item_resource_id: unique identifier of the target subscription item resource.
        :param resources: JSON representation of an object (subscription item resource) that should be created.
        """
        return self._get(
            "AddSubscriptionItemResource",
            params={
                "subscriptionId": subscription_id,
                "itemId": item_id,
                "itemResourceId": item_resource_id,
                "resources": resources,
            },
            delimiter=",",
        )

    def AdjustProduct(
        self,
        subscription_id: int,
        item_id: int,
        item_resource_id: int,
    ):
        """
        :param subscription_id: unique identifier of the target subscription.
        :param item_id: unique identifier of the target subscription item.
        :param item_resource_id: unique identifier of the target subscription item resource.
        """
        return self._get(
            "AdjustProduct",
            params={
                "subscriptionId": subscription_id,
                "itemId": item_id,
                "itemResourceId": item_resource_id,
            },
        )

    def DeleteCategory(
        self,
        id: int,
        reseller_id: list[int] = None,
    ):
        """
        :param id: unique identifier of the target category.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "DeleteCategory",
            params={"id": id, "resellerId": reseller_id},
            delimiter=",",
        )

    def DeleteProduct(
        self,
        id: int,
        reseller_id: list[int] = None,
    ):
        """
        :param id: unique identifier of the target product.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "DeleteProduct",
            params={"id": id, "resellerId": reseller_id},
            delimiter=",",
        )

    def DeleteServicePlan(
        self,
        id: int,
        reseller_id: list[int] = None,
    ):
        """
        :param id: unique identifier of the target service plan.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "DeleteServicePlan",
            params={"id": id, "resellerId": reseller_id},
            delimiter=",",
        )

    def EditCategory(self, category: dict, reseller_id: list[int] = None):
        """
        :param category: JSON representation of an object (subscription Category) that should be created.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "EditCategory",
            params={
                "category": category,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def EditProduct(self, category: dict, reseller_id: list[int] = None):
        """
        :param category: JSON representation of an object (subscription Product) that should be created.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "EditProduct",
            params={
                "category": category,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def EditServicePlan(
        self,
        service_plan: dict,
        reseller_id: list[int] = None,
        expend_fields: list[str] = None,
    ):
        """
        :param service_plan: JSON representation of an object (subscription Service Plan) that should be created.
        :param reseller_id: unique identifier of the target reseller platform.
        :param expend_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        """
        return self._get(
            "EditServicePlan",
            params={
                "servicePlan": service_plan,
                "resellerId": reseller_id,
                "expendFields": expend_fields,
            },
            delimiter=",",
        )

    def GetCategories(
        self,
        reseller_id: list[int] = None,
        expend_fields: list[str] = None,
    ):
        """
        :param reseller_id: unique identifier of the target reseller platform.
        :param expend_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        """
        return self._get(
            "GetCategories",
            params={
                "resellerId": reseller_id,
                "expendFields": expend_fields,
            },
            delimiter=",",
        )

    def GetProducts(
        self,
        id: list[int] = None,
        status: list[str] = None,
        reseller_id: list[int] = None,
        subscription_status: list[str] = None,
        expend_fields: list[str] = None,
        start_row: list[int] = None,
        result_count: list[int] = None,
        order_field: list[str] = None,
        order_direction: list[str] = None,
    ):
        """
        :param id: unique identifier of the product (for filtering).
        :param status: a comma-separated list of the subscription Product statuses (ProductStatus) that should be returned.
        :param reseller_id: unique identifier of the target reseller platform.
        :param subscription_status: a comma-separated list of the subscription statuses (SubscriptionStatus) that should be returned.
        :param expend_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        :param start_row: returns information starting from the specified row in the response (starts with 0, by default).
        :param result_count: returns the specified number of rows from the response (0 – unlimited – by default).
        :param order_field: sorts results by the specified field
        :param order_direction: sorts results in the ascending (ASC) or descending (DESC) order
        """
        return self._get(
            "GetProduct",
            params={
                "id": id,
                "status": status,
                "resellerId": reseller_id,
                "subscriptionStatus": subscription_status,
                "expandFields": expend_fields,
                "startRow": start_row,
                "resultCount": result_count,
                "orderField": order_field,
                "orderDirection": order_direction,
            },
            delimiter=",",
        )

    def GetServicePlans(
        self,
        id: list[int] = None,
        has_products: list[bool] = None,
        subscription_status: list[str] = None,
        product_id: list[int] = None,
        expend_fields: list[str] = None,
        reseller_id: list[int] = None,
    ):
        """
        :param id: unique identifier of the service plan (for filtering).
        :param has_products: a flag that indicates if returned Service Plans should have (true) or not (false) assigned products
        :param subscription_status: a comma-separated list of the subscription statuses (SubscriptionStatus) that should be returned.
        :param product_id: unique identifier of the subscription product (for filtering).
        :param expend_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "GetServicePlans",
            params={
                "id": id,
                "hasProducts": has_products,
                "subscriptionStatus": subscription_status,
                "productId": product_id,
                "expandFields": expend_fields,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def GetSubscriptions(
        self,
        id: list[int] = None,
        uid: list[int] = None,
        status: list[str] = None,
        reseller_id: list[int] = None,
        product_id: list[int] = None,
        service_plan_id: list[int] = None,
        expend_fields: list[str] = None,
        start_row: list[int] = None,
        result_count: list[int] = None,
        order_field: list[str] = None,
        order_direction: list[str] = None,
    ):
        """
        :param id: unique identifier of the subscription (for filtering).
        :param uid: unique identifier of the target user.
        :param status: a comma-separated list of the subscription statuses (SubscriptionStatus) that should be returned.
        :param reseller_id: unique identifier of the target reseller platform.
        :param product_id: unique identifier of the target product.
        :param service_plan_id: unique identifier of the target service plan.
        :param expend_fields: there are fields that are not included in responses by default. You can request these fields as an expanded response by listing required object paths in this parameter (e.g. account.group).
        :param start_row: returns information starting from the specified row in the response (starts with 0, by default).
        :param result_count: returns the specified number of rows from the response (0 – unlimited – by default).
        :param order_field: sorts results by the specified field
        :param order_direction: sorts results in the ascending (ASC) or descending (DESC) order
        """
        return self._get(
            "GetSubscriptions",
            params={
                "id": id,
                "uid": uid,
                "status": status,
                "resellerId": reseller_id,
                "productId": product_id,
                "servicePlanId": service_plan_id,
                "expandFields": expend_fields,
                "startRow": start_row,
                "resultCount": result_count,
                "orderField": order_field,
                "orderDirection": order_direction,
            },
            delimiter=",",
        )

    def SetCategoryPublished(
        self,
        id: int,
        published: bool,
        reseller_id: list[int] = None,
    ):
        """
        :param id: unique identifier of the target category.
        :param published: publishes (true) or unpublishes (false) the subscription Category.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "SetCategoryPublished",
            params={
                "id": id,
                "published": published,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def SetProductStatus(
        self,
        id: int,
        status: str,
        reseller_id: list[int] = None,
    ):
        """
        :param id: unique identifier of the target product.
        :param status: a new status (ProductStatus) that should be set for the subscription Product.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "SetProductStatus",
            params={
                "id": id,
                "status": status,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def SetServicePlanStatus(
        self,
        id: int,
        status: str,
        reseller_id: list[int] = None,
    ):
        """
        :param id: unique identifier of the target service plan.
        :param status: a new status (ServicePlanStatus) that should be set for the subscription Service Plan.
        :param reseller_id: unique identifier of the target reseller platform.
        """
        return self._get(
            "SetServicePlanStatus",
            params={
                "id": id,
                "status": status,
                "resellerId": reseller_id,
            },
            delimiter=",",
        )

    def TerminateSubscription(
        self,
        subscription_id: int,
        password: str,
    ):
        """
        :param subscription_id: unique identifier of the target subscription.
        :param password: current (admin) user's password to confirm subscription resources deletion.
        """
        return self._get(
            "TerminateSubscription",
            params={
                "subscriptionId": subscription_id,
                "password": password,
            },
        )
