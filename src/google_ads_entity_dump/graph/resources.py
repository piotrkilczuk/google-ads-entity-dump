from google.ads.googleads.v11.resources.types import (
    campaign,
    ad_group,
    accessible_bidding_strategy,
    account_budget,
    account_budget_proposal,
    billing_setup,
    account_link,
    ad_group_ad,
    ad_group_ad_label,
    label,
    ad_group_asset,
    asset,
    ad_group_bid_modifier,
    ad_group_criterion,
)

from google_ads_entity_dump.graph.abstract import *


graph = Graph()

# https://developers.google.com/google-ads/api/reference/rpc/v11/overview

# @TODO: Embedded messages, e.g. AccessibleBiddingStrategy.MaximizeConversionValue have all been ignored for now

AccessibleBiddingStrategy = Node(accessible_bidding_strategy.AccessibleBiddingStrategy, graph)

AccountBudget = Node(account_budget.AccountBudget, graph)

AccountBudgetProposal = Node(account_budget_proposal.AccountBudgetProposal, graph)
symmetric_many_to_one(AccountBudgetProposal, AccountBudget)

AccountLink = Node(account_link.AccountLink, graph)

# Ad = Node(ad.Ad)  @ TODO: how to model this since it's embedded in the AdGroupAd?

AdGroup = Node(ad_group.AdGroup, graph)
# AdGroup.base_ad_group ignored for now

AdGroupAd = Node(ad_group_ad.AdGroupAd, graph)
symmetric_many_to_one(AdGroupAd, AdGroup)  # @TODO: Unsure

# AdGroupAdAssetView  # @TODO: 'output only'

AdGroupAdLabel = Node(ad_group_ad_label.AdGroupAdLabel, graph)
symmetric_many_to_one(AdGroupAdLabel, AdGroupAd)

# AdGroupAdPolicySummary  # @TODO: 'output only'

AdGroupAsset = Node(ad_group_asset.AdGroupAsset, graph)
symmetric_many_to_one(AdGroupAsset, AdGroup)

# AdGroupAudienceView  # @TODO: 'output only'

AdGroupBidModifier = Node(ad_group_bid_modifier.AdGroupBidModifier, graph)
symmetric_many_to_one(AdGroupBidModifier, AdGroup)

AdGroupCriterion = Node(ad_group_criterion.AdGroupCriterion, graph)
symmetric_many_to_one(AdGroupCriterion, AdGroup)

Asset = Node(asset.Asset, graph)
symmetric_one_to_many(Asset, AdGroupAsset)

BillingSetup = Node(billing_setup.BillingSetup, graph)
symmetric_one_to_many(BillingSetup, AccountBudgetProposal)

Campaign = Node(campaign.Campaign, graph)
symmetric_one_to_many(Campaign, AdGroup)

Label = Node(label.Label, graph)
symmetric_one_to_many(Label, AdGroupAdLabel)
