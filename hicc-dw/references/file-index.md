# 模型代码文件索引（dbt 结构）

> 仓库: hicc_dw_script | 目录: `hicc_data_platform/models/` | 生成: 2026-09-09
> 物理表名 = 模型名（dbt alias），目标库: `hiccpet-481303.{dim|dwd|dws}`
> 代码仓库 GitHub 路径: `hicc_data_platform/models/{目录}/{文件名}`


## 01_trd 交易与销售

### dwd (8 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dwd_trd_channel_sku_sales_di.sql | `dwd.dwd_trd_channel_sku_sales_di` |
| dwd_trd_tob_hktvmall_order_item_di.sql | `dwd.dwd_trd_tob_hktvmall_order_item_di` |
| dwd_trd_toc_amazon_order_item_di.sql | `dwd.dwd_trd_toc_amazon_order_item_di` |
| dwd_trd_toc_lazada_order_item_di.sql | `dwd.dwd_trd_toc_lazada_order_item_di` |
| dwd_trd_toc_shopee_order_item_di.sql | `dwd.dwd_trd_toc_shopee_order_item_di` |
| dwd_trd_toc_shopify_order_item_di.sql | `dwd.dwd_trd_toc_shopify_order_item_di` |
| dwd_trd_toc_tk_order_item_di.sql | `dwd.dwd_trd_toc_tk_order_item_di` |
| dwd_trd_toc_walmart_order_item_di.sql | `dwd.dwd_trd_toc_walmart_order_item_di` |

### dws (1 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dws_trd_channel_sku_sales_di.sql | `dws.dws_trd_channel_sku_sales_di` |

## 02_mkt 营销与广告

### dim (2 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dim_mkt_amazon_sb_campaign_config.sql | `dim.dim_mkt_amazon_sb_campaign_config` |
| dim_mkt_campaign.sql | `dim.dim_mkt_campaign` |

### dwd (14 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dwd_mkt_amazon_ad_perf_di.sql | `dwd.dwd_mkt_amazon_ad_perf_di` |
| dwd_mkt_campaign_product_perf_di.sql | `dwd.dwd_mkt_campaign_product_perf_di` |
| dwd_mkt_chewy_ad_spend_di.sql | `dwd.dwd_mkt_chewy_ad_spend_di` |
| dwd_mkt_chewy_campaign_perf_di.sql | `dwd.dwd_mkt_chewy_campaign_perf_di` |
| dwd_mkt_chewy_campaign_sidebar_di.sql | `dwd.dwd_mkt_chewy_campaign_sidebar_di` |
| dwd_mkt_chewy_keyword_perf_di.sql | `dwd.dwd_mkt_chewy_keyword_perf_di` |
| dwd_mkt_chewy_offsite_campaign_perf_di.sql | `dwd.dwd_mkt_chewy_offsite_campaign_perf_di` |
| dwd_mkt_chewy_onsite_campaign_perf_di.sql | `dwd.dwd_mkt_chewy_onsite_campaign_perf_di` |
| dwd_mkt_lazada_adgroup_perf_di.sql | `dwd.dwd_mkt_lazada_adgroup_perf_di` |
| dwd_mkt_petco_ad_spend_di.sql | `dwd.dwd_mkt_petco_ad_spend_di` |
| dwd_mkt_shopee_campaign_perf_di.sql | `dwd.dwd_mkt_shopee_campaign_perf_di` |
| dwd_mkt_shopify_ga4_spend_di.sql | `dwd.dwd_mkt_shopify_ga4_spend_di` |
| dwd_mkt_tk_item_group_perf_di.sql | `dwd.dwd_mkt_tk_item_group_perf_di` |
| dwd_mkt_walmart_campaign_perf_di.sql | `dwd.dwd_mkt_walmart_campaign_perf_di` |

### dws (3 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dws_mkt_global_ad_spend_di.sql | `dws.dws_mkt_global_ad_spend_di` |
| dws_mkt_lazada_adgroup_perf_di.sql | `dws.dws_mkt_lazada_adgroup_perf_di` |
| dws_mkt_shopee_campaign_perf_di.sql | `dws.dws_mkt_shopee_campaign_perf_di` |

## 03_prd 产品与商品

### dim (6 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dim_prd_lazada_products.sql | `dim.dim_prd_lazada_products` |
| dim_prd_lingxing_amazon_product.sql | `dim.dim_prd_lingxing_amazon_product` |
| dim_prd_shipout_product.sql | `dim.dim_prd_shipout_product` |
| dim_prd_shopee_model.sql | `dim.dim_prd_shopee_model` |
| dim_prd_shopify_variants.sql | `dim.dim_prd_shopify_variants` |
| dim_prd_tk_products.sql | `dim.dim_prd_tk_products` |

### dwd (3 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dwd_prd_amazon_product_perf_di.sql | `dwd.dwd_prd_amazon_product_perf_di` |
| dwd_prd_amazon_seller_sku_di.sql | `dwd.dwd_prd_amazon_seller_sku_di` |
| dwd_prd_amazon_seller_sku_snap.sql | `dwd.dwd_prd_amazon_seller_sku_snap` |

## 04_ful 履约与交付

### dwd (1 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dwd_ful_amazon_shipment_di.sql | `dwd.dwd_ful_amazon_shipment_di` |

## 05_inv 库存与周转

### dim (2 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dim_amazon_shop_mapping.sql | `dim.dim_amazon_shop_mapping` |
| dim_inv_warehouse_attr.sql | `dim.dim_inv_warehouse_attr` |

### dwd (59 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dwd_inv_amazon_fba_stock_di.sql | `dwd.dwd_inv_amazon_fba_stock_di` |
| dwd_inv_amazon_fba_stock_snap.sql | `dwd.dwd_inv_amazon_fba_stock_snap` |
| dwd_inv_amazon_fba_stock_v2_snap.sql | `dwd.dwd_inv_amazon_fba_stock_v2_snap` |
| dwd_inv_amazon_inbound_txn_di.sql | `dwd.dwd_inv_amazon_inbound_txn_di` |
| dwd_inv_amazon_removal_shipment_di.sql | `dwd.dwd_inv_amazon_removal_shipment_di` |
| dwd_inv_amazon_removal_shipment_snap.sql | `dwd.dwd_inv_amazon_removal_shipment_snap` |
| dwd_inv_amazon_removal_shipment_v2_snap.sql | `dwd.dwd_inv_amazon_removal_shipment_v2_snap` |
| dwd_inv_chinese_stock_di.sql | `dwd.dwd_inv_chinese_stock_di` |
| dwd_inv_chinese_stock_snap.sql | `dwd.dwd_inv_chinese_stock_snap` |
| dwd_inv_chinese_stock_v2_snap.sql | `dwd.dwd_inv_chinese_stock_v2_snap` |
| dwd_inv_dbeehk_available_stock_di.sql | `dwd.dwd_inv_dbeehk_available_stock_di` |
| dwd_inv_dbeehk_inbound_details_snap.sql | `dwd.dwd_inv_dbeehk_inbound_details_snap` |
| dwd_inv_dbeehk_inbound_txn_di.sql | `dwd.dwd_inv_dbeehk_inbound_txn_di` |
| dwd_inv_dbeehk_inbound_v2_snap.sql | `dwd.dwd_inv_dbeehk_inbound_v2_snap` |
| dwd_inv_dbeehk_intransit_stock_di.sql | `dwd.dwd_inv_dbeehk_intransit_stock_di` |
| dwd_inv_dbeehk_stock_snap.sql | `dwd.dwd_inv_dbeehk_stock_snap` |
| dwd_inv_dbeehk_stock_v2_snap.sql | `dwd.dwd_inv_dbeehk_stock_v2_snap` |
| dwd_inv_feishu_warehouse_sg_value_snap.sql | `dwd.dwd_inv_feishu_warehouse_sg_value_snap` |
| dwd_inv_global_detail_v2_snap.sql | `dwd.dwd_inv_global_detail_v2_snap` |
| dwd_inv_inbound_shipment_status_di.sql | `dwd.dwd_inv_inbound_shipment_status_di` |
| dwd_inv_locad_inbound_txn_di.sql | `dwd.dwd_inv_locad_inbound_txn_di` |
| dwd_inv_locad_stock_di.sql | `dwd.dwd_inv_locad_stock_di` |
| dwd_inv_locad_stock_snap.sql | `dwd.dwd_inv_locad_stock_snap` |
| dwd_inv_locad_stock_v2_snap.sql | `dwd.dwd_inv_locad_stock_v2_snap` |
| dwd_inv_loho_available_stock_di.sql | `dwd.dwd_inv_loho_available_stock_di` |
| dwd_inv_loho_inbound_list_snap.sql | `dwd.dwd_inv_loho_inbound_list_snap` |
| dwd_inv_loho_inbound_txn_di.sql | `dwd.dwd_inv_loho_inbound_txn_di` |
| dwd_inv_loho_inbound_v2_snap.sql | `dwd.dwd_inv_loho_inbound_v2_snap` |
| dwd_inv_loho_intransit_stock_di.sql | `dwd.dwd_inv_loho_intransit_stock_di` |
| dwd_inv_loho_stock_snap.sql | `dwd.dwd_inv_loho_stock_snap` |
| dwd_inv_loho_stock_v2_snap.sql | `dwd.dwd_inv_loho_stock_v2_snap` |
| dwd_inv_maple_inbound_txn_di.sql | `dwd.dwd_inv_maple_inbound_txn_di` |
| dwd_inv_maple_stock_di.sql | `dwd.dwd_inv_maple_stock_di` |
| dwd_inv_maple_stock_snap.sql | `dwd.dwd_inv_maple_stock_snap` |
| dwd_inv_maple_stock_v2_snap.sql | `dwd.dwd_inv_maple_stock_v2_snap` |
| dwd_inv_scm_undelivered_order_details_snap.sql | `dwd.dwd_inv_scm_undelivered_order_details_snap` |
| dwd_inv_shipout_inbound_order_di.sql | `dwd.dwd_inv_shipout_inbound_order_di` |
| dwd_inv_shipout_inbound_order_snap.sql | `dwd.dwd_inv_shipout_inbound_order_snap` |
| dwd_inv_shipout_inbound_stock_di.sql | `dwd.dwd_inv_shipout_inbound_stock_di` |
| dwd_inv_shipout_inbound_stock_snap.sql | `dwd.dwd_inv_shipout_inbound_stock_snap` |
| dwd_inv_shipout_inbound_txn_di.sql | `dwd.dwd_inv_shipout_inbound_txn_di` |
| dwd_inv_shipout_inbound_v2_snap.sql | `dwd.dwd_inv_shipout_inbound_v2_snap` |
| dwd_inv_tk_fbt_stock_di.sql | `dwd.dwd_inv_tk_fbt_stock_di` |
| dwd_inv_tk_fbt_stock_snap.sql | `dwd.dwd_inv_tk_fbt_stock_snap` |
| dwd_inv_tk_fbt_stock_v2_snap.sql | `dwd.dwd_inv_tk_fbt_stock_v2_snap` |
| dwd_inv_tk_inbound_txn_di.sql | `dwd.dwd_inv_tk_inbound_txn_di` |
| dwd_inv_walmart_inbound_txn_di.sql | `dwd.dwd_inv_walmart_inbound_txn_di` |
| dwd_inv_walmart_wfs_stock_di.sql | `dwd.dwd_inv_walmart_wfs_stock_di` |
| dwd_inv_walmart_wfs_stock_snap.sql | `dwd.dwd_inv_walmart_wfs_stock_snap` |
| dwd_inv_walmart_wfs_stock_v2_snap.sql | `dwd.dwd_inv_walmart_wfs_stock_v2_snap` |
| dwd_inv_warehouse_outbound_di.sql | `dwd.dwd_inv_warehouse_outbound_di` |
| dwd_inv_winit_inbound_order_di.sql | `dwd.dwd_inv_winit_inbound_order_di` |
| dwd_inv_winit_inbound_txn_di.sql | `dwd.dwd_inv_winit_inbound_txn_di` |
| dwd_inv_winit_inventory_by_organization_snap.sql | `dwd.dwd_inv_winit_inventory_by_organization_snap` |
| dwd_inv_winit_inventory_by_type_snap.sql | `dwd.dwd_inv_winit_inventory_by_type_snap` |
| dwd_inv_winit_org_stock_di.sql | `dwd.dwd_inv_winit_org_stock_di` |
| dwd_inv_winit_stock_v2_snap.sql | `dwd.dwd_inv_winit_stock_v2_snap` |
| dwd_inv_winit_type_stock_di.sql | `dwd.dwd_inv_winit_type_stock_di` |
| dwd_scm_winit_outbound_di.sql | `dwd.dwd_scm_winit_outbound_di` |

### dws (3 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dws_inv_global_inbound_txn_di.sql | `dws.dws_inv_global_inbound_txn_di` |
| dws_inv_global_stock_snap.sql | `dws.dws_inv_global_stock_snap` |
| dws_inv_inbound_shipment_info_di.sql | `dws.dws_inv_inbound_shipment_info_di` |

## 06_voc 客户与体验(退货)

### dwd (6 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dwd_voc_amazon_return_di.sql | `dwd.dwd_voc_amazon_return_di` |
| dwd_voc_hktvmall_return_di.sql | `dwd.dwd_voc_hktvmall_return_di` |
| dwd_voc_lazada_return_di.sql | `dwd.dwd_voc_lazada_return_di` |
| dwd_voc_shopee_return_di.sql | `dwd.dwd_voc_shopee_return_di` |
| dwd_voc_shopify_return_di.sql | `dwd.dwd_voc_shopify_return_di` |
| dwd_voc_walmart_return_di.sql | `dwd.dwd_voc_walmart_return_di` |

### dws (1 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dws_voc_global_return_di.sql | `dws.dws_voc_global_return_di` |

## 07_fnc 财务与核算

### dwd (7 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dwd_fnc_chewy_rebate_di.sql | `dwd.dwd_fnc_chewy_rebate_di` |
| dwd_fnc_ezzeship_postfee_di.sql | `dwd.dwd_fnc_ezzeship_postfee_di` |
| dwd_fnc_quickbooks_invoice_allocated_di.sql | `dwd.dwd_fnc_quickbooks_invoice_allocated_di` |
| dwd_fnc_quickbooks_invoice_di.sql | `dwd.dwd_fnc_quickbooks_invoice_di` |
| dwd_fnc_quickbooks_invoice_item_di.sql | `dwd.dwd_fnc_quickbooks_invoice_item_di` |
| dwd_fnc_sps_invoice_detail_di.sql | `dwd.dwd_fnc_sps_invoice_detail_di` |
| dwd_fnc_subject_records_di.sql | `dwd.dwd_fnc_subject_records_di` |

### dws (1 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dws_fnc_sps_order_flag_di.sql | `dws.dws_fnc_sps_order_flag_di` |

## 08_scm 采购与供应

### dim (4 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dim_scm_inbound_close_manual.sql | `dim.dim_scm_inbound_close_manual` |
| dim_scm_shipment_exclusive.sql | `dim.dim_scm_shipment_exclusive` |
| dim_scm_shipment_mapping.sql | `dim.dim_scm_shipment_mapping` |
| dim_scm_supplier.sql | `dim.dim_scm_supplier` |

### dwd (11 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dwd_scm_amazon_po_order_di.sql | `dwd.dwd_scm_amazon_po_order_di` |
| dwd_scm_amazon_po_order_snap.sql | `dwd.dwd_scm_amazon_po_order_snap` |
| dwd_scm_b2b_po_import_di.sql | `dwd.dwd_scm_b2b_po_import_di` |
| dwd_scm_lingxing_purchase_receipt_di.sql | `dwd.dwd_scm_lingxing_purchase_receipt_di` |
| dwd_scm_shipment_order_di.sql | `dwd.dwd_scm_shipment_order_di` |
| dwd_scm_shipment_order_extend_di.sql | `dwd.dwd_scm_shipment_order_extend_di` |
| dwd_scm_shipment_track_dates_di.sql | `dwd.dwd_scm_shipment_track_dates_di` |
| dwd_scm_shipment_track_node_di.sql | `dwd.dwd_scm_shipment_track_node_di` |
| dwd_scm_shipout_billing_txn_di.sql | `dwd.dwd_scm_shipout_billing_txn_di` |
| dwd_scm_shipout_outbound_txn_di.sql | `dwd.dwd_scm_shipout_outbound_txn_di` |
| dwd_scm_sps_po_detail_di.sql | `dwd.dwd_scm_sps_po_detail_di` |

### dws (3 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dws_scm_shipment_abnormal_data_di.sql | `dws.dws_scm_shipment_abnormal_data_di` |
| dws_scm_shipping_sla_percentile_snap.sql | `dws.dws_scm_shipping_sla_percentile_snap` |
| dws_scm_sps_po_detail_di.sql | `dws.dws_scm_sps_po_detail_di` |

## 09_mdm 主数据与维度

### dim (21 个 SQL)
| 文件名 | 目标表(物理) |
|--------|-------------|
| dim_business_channel_v2.sql | `dim.dim_business_channel_v2` |
| dim_calendar_cn.sql | `dim.dim_calendar_cn` |
| dim_calendar_local.sql | `dim.dim_calendar_local` |
| dim_channel_lingxing_account.sql | `dim.dim_channel_lingxing_account` |
| dim_country_v2.sql | `dim.dim_country_v2` |
| dim_date.sql | `dim.dim_date` |
| dim_exchange_rates.sql | `dim.dim_exchange_rates` |
| dim_hicc_sku_mapping_v2.sql | `dim.dim_hicc_sku_mapping_v2` |
| dim_import_sku_mapping.sql | `dim.dim_import_sku_mapping` |
| dim_mkt_petco_creative_mapping.sql | `dim.dim_mkt_petco_creative_mapping` |
| dim_prd_bundle_info.sql | `dim.dim_prd_bundle_info` |
| dim_prd_sps_vendor_style.sql | `dim.dim_prd_sps_vendor_style` |
| dim_product_categories.sql | `dim.dim_product_categories` |
| dim_product_skus.sql | `dim.dim_product_skus` |
| dim_product_skus_purchase.sql | `dim.dim_product_skus_purchase` |
| dim_product_skus_sales.sql | `dim.dim_product_skus_sales` |
| dim_product_skus_warehouse.sql | `dim.dim_product_skus_warehouse` |
| dim_scm_shipping_time.sql | `dim.dim_scm_shipping_time` |
| dim_shop_v2.sql | `dim.dim_shop_v2` |
| dim_sku_mapping.sql | `dim.dim_sku_mapping` |
| dim_warehouse_sku_mapping.sql | `dim.dim_warehouse_sku_mapping` |