import json
from typing import List, Any, Optional
from fastapi import UploadFile
default_state = json.loads('{"p_Home_Flex1_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex2_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex4_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex138_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_TextBox1_bpt":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_TextBox2_bpt":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_TextBox6_bpt":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_TextBox4_bpt":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_TextBox3_bpt":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex3_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex5_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex6_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_TextBox9_bpt":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex8_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex9_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex10_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_TextBox7_bpt":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_TextBox8_bpt":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex7_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex11_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex12_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex371_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex373_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex13_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex14_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex365_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex15_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex366_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex367_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex21_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex368_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex25_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex26_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex27_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex29_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex30_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex35_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex32_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex28_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex37_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p__Home_Flex38_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex39_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex40_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex297_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Product_Card_1_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex42_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Product_Card_2_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex43_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex298_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Product_Card_4_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex47_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Product_Card_3_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex45_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex58_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex57_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex300_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Product_Card_7_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex50_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Product_Card_8_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex49_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex299_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Product_Card_6_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex51_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Product_Card_5_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex52_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex59_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex60_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex62_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex61_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex63_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex130_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex89_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex128_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex64_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex65_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex131_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex132_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex133_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex134_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex1315_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex67_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex68_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex129_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex69_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex71_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex72_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex73_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex74_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex75_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex76_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex77_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex81_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex82_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex85_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex83_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex84_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex90_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex92_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex98_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex99_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex100_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex101_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex104_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex103_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex102_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex107_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex106_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex105_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex108_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex91_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex93_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex94_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex95_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex110_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex112_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex111_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex113_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex114_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex115_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex116_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex117_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex118_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex121_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex119_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex125_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex127_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex120_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex124_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex123_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Flex122_bpt":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"p_Home_Image2_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox4":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox5":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox8":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox7":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox6":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Button1_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"p_Home_Button2_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"TextBox11":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Button3_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"p_Home_Button4_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"TextBox9":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox10":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image5_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox12":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image6_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image10_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image198_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image197_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox11_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image11_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox13_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox14_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox12_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image195_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox383_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox384_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox382_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox32_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox30_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox31_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image17_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image196_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox386_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox387_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox385_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Button9_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"p_Home_Button10_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"p_Home_Image19_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox36_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image20_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox38_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image25_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox43_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image22_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox40_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox44_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox45_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox46_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Button12_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"p_Home_Button11_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"p_Home_TextBox47_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox48_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Name_1_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_About_1_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Image_1_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Product_Price_1_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Image_2_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Product_About_2_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Name_2_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Price_2_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Name_4_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_About_4_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Image_4_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Product_Price_4_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Image_3_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Product_About_3_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Name_3_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Price_3_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Button14_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"p_Home_Button13_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"p_Home_Product_Name_7_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_About_7_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Image_7_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Product_Price_7_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Image_8_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Product_About_8_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Name_8_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Price_8_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Name_6_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox67":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Image_6_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Product_Price_6_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Image_5_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Product_About_5_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Name_5_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Product_Price_5_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox73_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox74_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Button16_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"p_Home_Button15_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"p_Home_Image34_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox75_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox76_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox142_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image74_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox78_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox79_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image44_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image76_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image77_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image78_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image79_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image40_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox81_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox80_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image75_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Button17_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"p_Home_Button18_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"p_Home_TextBox82_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox83_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image45_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox85_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox86_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox84_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image49_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox97_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox96_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox100_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox99":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image51_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image52_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox102_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox101_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox104":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox103_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image53_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Button21_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"p_Home_TextBox113_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Input1_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"value":"","placeholder":"","isPasswordField":false}},"p_Home_Input2_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"value":"","placeholder":"","isPasswordField":false}},"p_Home_TextBox114_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Input4_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"value":"","placeholder":"","isPasswordField":false}},"p_Home_TextBox116_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Input3_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"value":"","placeholder":"","isPasswordField":false}},"p_Home_TextBox115_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox118_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Input6_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"value":"","placeholder":"","isPasswordField":false}},"p_Home_TextBox117_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Input5_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"value":"","placeholder":"","isPasswordField":false}},"p_Home_TextBox120_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Input9_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"value":"","placeholder":"","isPasswordField":false}},"p_Home_TextBox105_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox106_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image54_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox107_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image55_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox111_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image56_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox112_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox122_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox121_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image58_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image59_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image61_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image60_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image63_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image62_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image64_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox123_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image65_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image66_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image67_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image68_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image69_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_TextBox125_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox126_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox127_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox128_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox129_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox130_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox131_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox133_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox134_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox139_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox138_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox137_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox136_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox135_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox140_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox141_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_TextBox124_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"p_Home_Image72_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image73_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image70_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"p_Home_Image71_bpt":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}}}')
def get_defined_value(state, def_state, key):
	return state[key] if key in state else def_state[key]
class Atri:
	def __init__(self, state: Any):
		self.event_data = None
		self.event_alias = None
		global default_state
		self._setter_access_tracker = {}
		self.p_Home_Flex1_bpt = state["p_Home_Flex1_bpt"]
		self.p_Home_Flex2_bpt = state["p_Home_Flex2_bpt"]
		self.p_Home_Flex4_bpt = state["p_Home_Flex4_bpt"]
		self.p_Home_Flex138_bpt = state["p_Home_Flex138_bpt"]
		self.p_Home_TextBox1_bpt = state["p_Home_TextBox1_bpt"]
		self.p_Home_TextBox2_bpt = state["p_Home_TextBox2_bpt"]
		self.p_Home_TextBox6_bpt = state["p_Home_TextBox6_bpt"]
		self.p_Home_TextBox4_bpt = state["p_Home_TextBox4_bpt"]
		self.p_Home_TextBox3_bpt = state["p_Home_TextBox3_bpt"]
		self.p_Home_Flex3_bpt = state["p_Home_Flex3_bpt"]
		self.p_Home_Flex5_bpt = state["p_Home_Flex5_bpt"]
		self.p_Home_Flex6_bpt = state["p_Home_Flex6_bpt"]
		self.p_Home_TextBox9_bpt = state["p_Home_TextBox9_bpt"]
		self.p_Home_Flex8_bpt = state["p_Home_Flex8_bpt"]
		self.p_Home_Flex9_bpt = state["p_Home_Flex9_bpt"]
		self.p_Home_Flex10_bpt = state["p_Home_Flex10_bpt"]
		self.p_Home_TextBox7_bpt = state["p_Home_TextBox7_bpt"]
		self.p_Home_TextBox8_bpt = state["p_Home_TextBox8_bpt"]
		self.p_Home_Flex7_bpt = state["p_Home_Flex7_bpt"]
		self.p_Home_Flex11_bpt = state["p_Home_Flex11_bpt"]
		self.p_Home_Flex12_bpt = state["p_Home_Flex12_bpt"]
		self.p_Home_Flex371_bpt = state["p_Home_Flex371_bpt"]
		self.p_Home_Flex373_bpt = state["p_Home_Flex373_bpt"]
		self.p_Home_Flex13_bpt = state["p_Home_Flex13_bpt"]
		self.p_Home_Flex14_bpt = state["p_Home_Flex14_bpt"]
		self.p_Home_Flex365_bpt = state["p_Home_Flex365_bpt"]
		self.p_Home_Flex15_bpt = state["p_Home_Flex15_bpt"]
		self.p_Home_Flex366_bpt = state["p_Home_Flex366_bpt"]
		self.p_Home_Flex367_bpt = state["p_Home_Flex367_bpt"]
		self.p_Home_Flex21_bpt = state["p_Home_Flex21_bpt"]
		self.p_Home_Flex368_bpt = state["p_Home_Flex368_bpt"]
		self.p_Home_Flex25_bpt = state["p_Home_Flex25_bpt"]
		self.p_Home_Flex26_bpt = state["p_Home_Flex26_bpt"]
		self.p_Home_Flex27_bpt = state["p_Home_Flex27_bpt"]
		self.p_Home_Flex29_bpt = state["p_Home_Flex29_bpt"]
		self.p_Home_Flex30_bpt = state["p_Home_Flex30_bpt"]
		self.p_Home_Flex35_bpt = state["p_Home_Flex35_bpt"]
		self.p_Home_Flex32_bpt = state["p_Home_Flex32_bpt"]
		self.p_Home_Flex28_bpt = state["p_Home_Flex28_bpt"]
		self.p_Home_Flex37_bpt = state["p_Home_Flex37_bpt"]
		self.p__Home_Flex38_bpt = state["p__Home_Flex38_bpt"]
		self.p_Home_Flex39_bpt = state["p_Home_Flex39_bpt"]
		self.p_Home_Flex40_bpt = state["p_Home_Flex40_bpt"]
		self.p_Home_Flex297_bpt = state["p_Home_Flex297_bpt"]
		self.p_Home_Product_Card_1_bpt = state["p_Home_Product_Card_1_bpt"]
		self.p_Home_Flex42_bpt = state["p_Home_Flex42_bpt"]
		self.p_Home_Product_Card_2_bpt = state["p_Home_Product_Card_2_bpt"]
		self.p_Home_Flex43_bpt = state["p_Home_Flex43_bpt"]
		self.p_Home_Flex298_bpt = state["p_Home_Flex298_bpt"]
		self.p_Home_Product_Card_4_bpt = state["p_Home_Product_Card_4_bpt"]
		self.p_Home_Flex47_bpt = state["p_Home_Flex47_bpt"]
		self.p_Home_Product_Card_3_bpt = state["p_Home_Product_Card_3_bpt"]
		self.p_Home_Flex45_bpt = state["p_Home_Flex45_bpt"]
		self.p_Home_Flex58_bpt = state["p_Home_Flex58_bpt"]
		self.p_Home_Flex57_bpt = state["p_Home_Flex57_bpt"]
		self.p_Home_Flex300_bpt = state["p_Home_Flex300_bpt"]
		self.p_Home_Product_Card_7_bpt = state["p_Home_Product_Card_7_bpt"]
		self.p_Home_Flex50_bpt = state["p_Home_Flex50_bpt"]
		self.p_Home_Product_Card_8_bpt = state["p_Home_Product_Card_8_bpt"]
		self.p_Home_Flex49_bpt = state["p_Home_Flex49_bpt"]
		self.p_Home_Flex299_bpt = state["p_Home_Flex299_bpt"]
		self.p_Home_Product_Card_6_bpt = state["p_Home_Product_Card_6_bpt"]
		self.p_Home_Flex51_bpt = state["p_Home_Flex51_bpt"]
		self.p_Home_Product_Card_5_bpt = state["p_Home_Product_Card_5_bpt"]
		self.p_Home_Flex52_bpt = state["p_Home_Flex52_bpt"]
		self.p_Home_Flex59_bpt = state["p_Home_Flex59_bpt"]
		self.p_Home_Flex60_bpt = state["p_Home_Flex60_bpt"]
		self.p_Home_Flex62_bpt = state["p_Home_Flex62_bpt"]
		self.p_Home_Flex61_bpt = state["p_Home_Flex61_bpt"]
		self.p_Home_Flex63_bpt = state["p_Home_Flex63_bpt"]
		self.p_Home_Flex130_bpt = state["p_Home_Flex130_bpt"]
		self.p_Home_Flex89_bpt = state["p_Home_Flex89_bpt"]
		self.p_Home_Flex128_bpt = state["p_Home_Flex128_bpt"]
		self.p_Home_Flex64_bpt = state["p_Home_Flex64_bpt"]
		self.p_Home_Flex65_bpt = state["p_Home_Flex65_bpt"]
		self.p_Home_Flex131_bpt = state["p_Home_Flex131_bpt"]
		self.p_Home_Flex132_bpt = state["p_Home_Flex132_bpt"]
		self.p_Home_Flex133_bpt = state["p_Home_Flex133_bpt"]
		self.p_Home_Flex134_bpt = state["p_Home_Flex134_bpt"]
		self.p_Home_Flex1315_bpt = state["p_Home_Flex1315_bpt"]
		self.p_Home_Flex67_bpt = state["p_Home_Flex67_bpt"]
		self.p_Home_Flex68_bpt = state["p_Home_Flex68_bpt"]
		self.p_Home_Flex129_bpt = state["p_Home_Flex129_bpt"]
		self.p_Home_Flex69_bpt = state["p_Home_Flex69_bpt"]
		self.p_Home_Flex71_bpt = state["p_Home_Flex71_bpt"]
		self.p_Home_Flex72_bpt = state["p_Home_Flex72_bpt"]
		self.p_Home_Flex73_bpt = state["p_Home_Flex73_bpt"]
		self.p_Home_Flex74_bpt = state["p_Home_Flex74_bpt"]
		self.p_Home_Flex75_bpt = state["p_Home_Flex75_bpt"]
		self.p_Home_Flex76_bpt = state["p_Home_Flex76_bpt"]
		self.p_Home_Flex77_bpt = state["p_Home_Flex77_bpt"]
		self.p_Home_Flex81_bpt = state["p_Home_Flex81_bpt"]
		self.p_Home_Flex82_bpt = state["p_Home_Flex82_bpt"]
		self.p_Home_Flex85_bpt = state["p_Home_Flex85_bpt"]
		self.p_Home_Flex83_bpt = state["p_Home_Flex83_bpt"]
		self.p_Home_Flex84_bpt = state["p_Home_Flex84_bpt"]
		self.p_Home_Flex90_bpt = state["p_Home_Flex90_bpt"]
		self.p_Home_Flex92_bpt = state["p_Home_Flex92_bpt"]
		self.p_Home_Flex98_bpt = state["p_Home_Flex98_bpt"]
		self.p_Home_Flex99_bpt = state["p_Home_Flex99_bpt"]
		self.p_Home_Flex100_bpt = state["p_Home_Flex100_bpt"]
		self.p_Home_Flex101_bpt = state["p_Home_Flex101_bpt"]
		self.p_Home_Flex104_bpt = state["p_Home_Flex104_bpt"]
		self.p_Home_Flex103_bpt = state["p_Home_Flex103_bpt"]
		self.p_Home_Flex102_bpt = state["p_Home_Flex102_bpt"]
		self.p_Home_Flex107_bpt = state["p_Home_Flex107_bpt"]
		self.p_Home_Flex106_bpt = state["p_Home_Flex106_bpt"]
		self.p_Home_Flex105_bpt = state["p_Home_Flex105_bpt"]
		self.p_Home_Flex108_bpt = state["p_Home_Flex108_bpt"]
		self.p_Home_Flex91_bpt = state["p_Home_Flex91_bpt"]
		self.p_Home_Flex93_bpt = state["p_Home_Flex93_bpt"]
		self.p_Home_Flex94_bpt = state["p_Home_Flex94_bpt"]
		self.p_Home_Flex95_bpt = state["p_Home_Flex95_bpt"]
		self.p_Home_Flex110_bpt = state["p_Home_Flex110_bpt"]
		self.p_Home_Flex112_bpt = state["p_Home_Flex112_bpt"]
		self.p_Home_Flex111_bpt = state["p_Home_Flex111_bpt"]
		self.p_Home_Flex113_bpt = state["p_Home_Flex113_bpt"]
		self.p_Home_Flex114_bpt = state["p_Home_Flex114_bpt"]
		self.p_Home_Flex115_bpt = state["p_Home_Flex115_bpt"]
		self.p_Home_Flex116_bpt = state["p_Home_Flex116_bpt"]
		self.p_Home_Flex117_bpt = state["p_Home_Flex117_bpt"]
		self.p_Home_Flex118_bpt = state["p_Home_Flex118_bpt"]
		self.p_Home_Flex121_bpt = state["p_Home_Flex121_bpt"]
		self.p_Home_Flex119_bpt = state["p_Home_Flex119_bpt"]
		self.p_Home_Flex125_bpt = state["p_Home_Flex125_bpt"]
		self.p_Home_Flex127_bpt = state["p_Home_Flex127_bpt"]
		self.p_Home_Flex120_bpt = state["p_Home_Flex120_bpt"]
		self.p_Home_Flex124_bpt = state["p_Home_Flex124_bpt"]
		self.p_Home_Flex123_bpt = state["p_Home_Flex123_bpt"]
		self.p_Home_Flex122_bpt = state["p_Home_Flex122_bpt"]
		self.p_Home_Image2_bpt = state["p_Home_Image2_bpt"]
		self.TextBox4 = state["TextBox4"]
		self.TextBox5 = state["TextBox5"]
		self.TextBox8 = state["TextBox8"]
		self.TextBox7 = state["TextBox7"]
		self.TextBox6 = state["TextBox6"]
		self.p_Home_Button1_bpt = state["p_Home_Button1_bpt"]
		self.p_Home_Button2_bpt = state["p_Home_Button2_bpt"]
		self.TextBox11 = state["TextBox11"]
		self.p_Home_Button3_bpt = state["p_Home_Button3_bpt"]
		self.p_Home_Button4_bpt = state["p_Home_Button4_bpt"]
		self.TextBox9 = state["TextBox9"]
		self.TextBox10 = state["TextBox10"]
		self.p_Home_Image5_bpt = state["p_Home_Image5_bpt"]
		self.TextBox12 = state["TextBox12"]
		self.p_Home_Image6_bpt = state["p_Home_Image6_bpt"]
		self.p_Home_Image10_bpt = state["p_Home_Image10_bpt"]
		self.p_Home_Image198_bpt = state["p_Home_Image198_bpt"]
		self.p_Home_Image197_bpt = state["p_Home_Image197_bpt"]
		self.p_Home_TextBox11_bpt = state["p_Home_TextBox11_bpt"]
		self.p_Home_Image11_bpt = state["p_Home_Image11_bpt"]
		self.p_Home_TextBox13_bpt = state["p_Home_TextBox13_bpt"]
		self.p_Home_TextBox14_bpt = state["p_Home_TextBox14_bpt"]
		self.p_Home_TextBox12_bpt = state["p_Home_TextBox12_bpt"]
		self.p_Home_Image195_bpt = state["p_Home_Image195_bpt"]
		self.p_Home_TextBox383_bpt = state["p_Home_TextBox383_bpt"]
		self.p_Home_TextBox384_bpt = state["p_Home_TextBox384_bpt"]
		self.p_Home_TextBox382_bpt = state["p_Home_TextBox382_bpt"]
		self.p_Home_TextBox32_bpt = state["p_Home_TextBox32_bpt"]
		self.p_Home_TextBox30_bpt = state["p_Home_TextBox30_bpt"]
		self.p_Home_TextBox31_bpt = state["p_Home_TextBox31_bpt"]
		self.p_Home_Image17_bpt = state["p_Home_Image17_bpt"]
		self.p_Home_Image196_bpt = state["p_Home_Image196_bpt"]
		self.p_Home_TextBox386_bpt = state["p_Home_TextBox386_bpt"]
		self.p_Home_TextBox387_bpt = state["p_Home_TextBox387_bpt"]
		self.p_Home_TextBox385_bpt = state["p_Home_TextBox385_bpt"]
		self.p_Home_Button9_bpt = state["p_Home_Button9_bpt"]
		self.p_Home_Button10_bpt = state["p_Home_Button10_bpt"]
		self.p_Home_Image19_bpt = state["p_Home_Image19_bpt"]
		self.p_Home_TextBox36_bpt = state["p_Home_TextBox36_bpt"]
		self.p_Home_Image20_bpt = state["p_Home_Image20_bpt"]
		self.p_Home_TextBox38_bpt = state["p_Home_TextBox38_bpt"]
		self.p_Home_Image25_bpt = state["p_Home_Image25_bpt"]
		self.p_Home_TextBox43_bpt = state["p_Home_TextBox43_bpt"]
		self.p_Home_Image22_bpt = state["p_Home_Image22_bpt"]
		self.p_Home_TextBox40_bpt = state["p_Home_TextBox40_bpt"]
		self.p_Home_TextBox44_bpt = state["p_Home_TextBox44_bpt"]
		self.p_Home_TextBox45_bpt = state["p_Home_TextBox45_bpt"]
		self.p_Home_TextBox46_bpt = state["p_Home_TextBox46_bpt"]
		self.p_Home_Button12_bpt = state["p_Home_Button12_bpt"]
		self.p_Home_Button11_bpt = state["p_Home_Button11_bpt"]
		self.p_Home_TextBox47_bpt = state["p_Home_TextBox47_bpt"]
		self.p_Home_TextBox48_bpt = state["p_Home_TextBox48_bpt"]
		self.p_Home_Product_Name_1_bpt = state["p_Home_Product_Name_1_bpt"]
		self.p_Home_Product_About_1_bpt = state["p_Home_Product_About_1_bpt"]
		self.p_Home_Product_Image_1_bpt = state["p_Home_Product_Image_1_bpt"]
		self.p_Home_Product_Price_1_bpt = state["p_Home_Product_Price_1_bpt"]
		self.p_Home_Product_Image_2_bpt = state["p_Home_Product_Image_2_bpt"]
		self.p_Home_Product_About_2_bpt = state["p_Home_Product_About_2_bpt"]
		self.p_Home_Product_Name_2_bpt = state["p_Home_Product_Name_2_bpt"]
		self.p_Home_Product_Price_2_bpt = state["p_Home_Product_Price_2_bpt"]
		self.p_Home_Product_Name_4_bpt = state["p_Home_Product_Name_4_bpt"]
		self.p_Home_Product_About_4_bpt = state["p_Home_Product_About_4_bpt"]
		self.p_Home_Product_Image_4_bpt = state["p_Home_Product_Image_4_bpt"]
		self.p_Home_Product_Price_4_bpt = state["p_Home_Product_Price_4_bpt"]
		self.p_Home_Product_Image_3_bpt = state["p_Home_Product_Image_3_bpt"]
		self.p_Home_Product_About_3_bpt = state["p_Home_Product_About_3_bpt"]
		self.p_Home_Product_Name_3_bpt = state["p_Home_Product_Name_3_bpt"]
		self.p_Home_Product_Price_3_bpt = state["p_Home_Product_Price_3_bpt"]
		self.p_Home_Button14_bpt = state["p_Home_Button14_bpt"]
		self.p_Home_Button13_bpt = state["p_Home_Button13_bpt"]
		self.p_Home_Product_Name_7_bpt = state["p_Home_Product_Name_7_bpt"]
		self.p_Home_Product_About_7_bpt = state["p_Home_Product_About_7_bpt"]
		self.p_Home_Product_Image_7_bpt = state["p_Home_Product_Image_7_bpt"]
		self.p_Home_Product_Price_7_bpt = state["p_Home_Product_Price_7_bpt"]
		self.p_Home_Product_Image_8_bpt = state["p_Home_Product_Image_8_bpt"]
		self.p_Home_Product_About_8_bpt = state["p_Home_Product_About_8_bpt"]
		self.p_Home_Product_Name_8_bpt = state["p_Home_Product_Name_8_bpt"]
		self.p_Home_Product_Price_8_bpt = state["p_Home_Product_Price_8_bpt"]
		self.p_Home_Product_Name_6_bpt = state["p_Home_Product_Name_6_bpt"]
		self.TextBox67 = state["TextBox67"]
		self.p_Home_Product_Image_6_bpt = state["p_Home_Product_Image_6_bpt"]
		self.p_Home_Product_Price_6_bpt = state["p_Home_Product_Price_6_bpt"]
		self.p_Home_Product_Image_5_bpt = state["p_Home_Product_Image_5_bpt"]
		self.p_Home_Product_About_5_bpt = state["p_Home_Product_About_5_bpt"]
		self.p_Home_Product_Name_5_bpt = state["p_Home_Product_Name_5_bpt"]
		self.p_Home_Product_Price_5_bpt = state["p_Home_Product_Price_5_bpt"]
		self.p_Home_TextBox73_bpt = state["p_Home_TextBox73_bpt"]
		self.p_Home_TextBox74_bpt = state["p_Home_TextBox74_bpt"]
		self.p_Home_Button16_bpt = state["p_Home_Button16_bpt"]
		self.p_Home_Button15_bpt = state["p_Home_Button15_bpt"]
		self.p_Home_Image34_bpt = state["p_Home_Image34_bpt"]
		self.p_Home_TextBox75_bpt = state["p_Home_TextBox75_bpt"]
		self.p_Home_TextBox76_bpt = state["p_Home_TextBox76_bpt"]
		self.p_Home_TextBox142_bpt = state["p_Home_TextBox142_bpt"]
		self.p_Home_Image74_bpt = state["p_Home_Image74_bpt"]
		self.p_Home_TextBox78_bpt = state["p_Home_TextBox78_bpt"]
		self.p_Home_TextBox79_bpt = state["p_Home_TextBox79_bpt"]
		self.p_Home_Image44_bpt = state["p_Home_Image44_bpt"]
		self.p_Home_Image76_bpt = state["p_Home_Image76_bpt"]
		self.p_Home_Image77_bpt = state["p_Home_Image77_bpt"]
		self.p_Home_Image78_bpt = state["p_Home_Image78_bpt"]
		self.p_Home_Image79_bpt = state["p_Home_Image79_bpt"]
		self.p_Home_Image40_bpt = state["p_Home_Image40_bpt"]
		self.p_Home_TextBox81_bpt = state["p_Home_TextBox81_bpt"]
		self.p_Home_TextBox80_bpt = state["p_Home_TextBox80_bpt"]
		self.p_Home_Image75_bpt = state["p_Home_Image75_bpt"]
		self.p_Home_Button17_bpt = state["p_Home_Button17_bpt"]
		self.p_Home_Button18_bpt = state["p_Home_Button18_bpt"]
		self.p_Home_TextBox82_bpt = state["p_Home_TextBox82_bpt"]
		self.p_Home_TextBox83_bpt = state["p_Home_TextBox83_bpt"]
		self.p_Home_Image45_bpt = state["p_Home_Image45_bpt"]
		self.p_Home_TextBox85_bpt = state["p_Home_TextBox85_bpt"]
		self.p_Home_TextBox86_bpt = state["p_Home_TextBox86_bpt"]
		self.p_Home_TextBox84_bpt = state["p_Home_TextBox84_bpt"]
		self.p_Home_Image49_bpt = state["p_Home_Image49_bpt"]
		self.p_Home_TextBox97_bpt = state["p_Home_TextBox97_bpt"]
		self.p_Home_TextBox96_bpt = state["p_Home_TextBox96_bpt"]
		self.p_Home_TextBox100_bpt = state["p_Home_TextBox100_bpt"]
		self.p_Home_TextBox99 = state["p_Home_TextBox99"]
		self.p_Home_Image51_bpt = state["p_Home_Image51_bpt"]
		self.p_Home_Image52_bpt = state["p_Home_Image52_bpt"]
		self.p_Home_TextBox102_bpt = state["p_Home_TextBox102_bpt"]
		self.p_Home_TextBox101_bpt = state["p_Home_TextBox101_bpt"]
		self.p_Home_TextBox104 = state["p_Home_TextBox104"]
		self.p_Home_TextBox103_bpt = state["p_Home_TextBox103_bpt"]
		self.p_Home_Image53_bpt = state["p_Home_Image53_bpt"]
		self.p_Home_Button21_bpt = state["p_Home_Button21_bpt"]
		self.p_Home_TextBox113_bpt = state["p_Home_TextBox113_bpt"]
		self.p_Home_Input1_bpt = state["p_Home_Input1_bpt"]
		self.p_Home_Input2_bpt = state["p_Home_Input2_bpt"]
		self.p_Home_TextBox114_bpt = state["p_Home_TextBox114_bpt"]
		self.p_Home_Input4_bpt = state["p_Home_Input4_bpt"]
		self.p_Home_TextBox116_bpt = state["p_Home_TextBox116_bpt"]
		self.p_Home_Input3_bpt = state["p_Home_Input3_bpt"]
		self.p_Home_TextBox115_bpt = state["p_Home_TextBox115_bpt"]
		self.p_Home_TextBox118_bpt = state["p_Home_TextBox118_bpt"]
		self.p_Home_Input6_bpt = state["p_Home_Input6_bpt"]
		self.p_Home_TextBox117_bpt = state["p_Home_TextBox117_bpt"]
		self.p_Home_Input5_bpt = state["p_Home_Input5_bpt"]
		self.p_Home_TextBox120_bpt = state["p_Home_TextBox120_bpt"]
		self.p_Home_Input9_bpt = state["p_Home_Input9_bpt"]
		self.p_Home_TextBox105_bpt = state["p_Home_TextBox105_bpt"]
		self.p_Home_TextBox106_bpt = state["p_Home_TextBox106_bpt"]
		self.p_Home_Image54_bpt = state["p_Home_Image54_bpt"]
		self.p_Home_TextBox107_bpt = state["p_Home_TextBox107_bpt"]
		self.p_Home_Image55_bpt = state["p_Home_Image55_bpt"]
		self.p_Home_TextBox111_bpt = state["p_Home_TextBox111_bpt"]
		self.p_Home_Image56_bpt = state["p_Home_Image56_bpt"]
		self.p_Home_TextBox112_bpt = state["p_Home_TextBox112_bpt"]
		self.p_Home_TextBox122_bpt = state["p_Home_TextBox122_bpt"]
		self.p_Home_TextBox121_bpt = state["p_Home_TextBox121_bpt"]
		self.p_Home_Image58_bpt = state["p_Home_Image58_bpt"]
		self.p_Home_Image59_bpt = state["p_Home_Image59_bpt"]
		self.p_Home_Image61_bpt = state["p_Home_Image61_bpt"]
		self.p_Home_Image60_bpt = state["p_Home_Image60_bpt"]
		self.p_Home_Image63_bpt = state["p_Home_Image63_bpt"]
		self.p_Home_Image62_bpt = state["p_Home_Image62_bpt"]
		self.p_Home_Image64_bpt = state["p_Home_Image64_bpt"]
		self.p_Home_TextBox123_bpt = state["p_Home_TextBox123_bpt"]
		self.p_Home_Image65_bpt = state["p_Home_Image65_bpt"]
		self.p_Home_Image66_bpt = state["p_Home_Image66_bpt"]
		self.p_Home_Image67_bpt = state["p_Home_Image67_bpt"]
		self.p_Home_Image68_bpt = state["p_Home_Image68_bpt"]
		self.p_Home_Image69_bpt = state["p_Home_Image69_bpt"]
		self.p_Home_TextBox125_bpt = state["p_Home_TextBox125_bpt"]
		self.p_Home_TextBox126_bpt = state["p_Home_TextBox126_bpt"]
		self.p_Home_TextBox127_bpt = state["p_Home_TextBox127_bpt"]
		self.p_Home_TextBox128_bpt = state["p_Home_TextBox128_bpt"]
		self.p_Home_TextBox129_bpt = state["p_Home_TextBox129_bpt"]
		self.p_Home_TextBox130_bpt = state["p_Home_TextBox130_bpt"]
		self.p_Home_TextBox131_bpt = state["p_Home_TextBox131_bpt"]
		self.p_Home_TextBox133_bpt = state["p_Home_TextBox133_bpt"]
		self.p_Home_TextBox134_bpt = state["p_Home_TextBox134_bpt"]
		self.p_Home_TextBox139_bpt = state["p_Home_TextBox139_bpt"]
		self.p_Home_TextBox138_bpt = state["p_Home_TextBox138_bpt"]
		self.p_Home_TextBox137_bpt = state["p_Home_TextBox137_bpt"]
		self.p_Home_TextBox136_bpt = state["p_Home_TextBox136_bpt"]
		self.p_Home_TextBox135_bpt = state["p_Home_TextBox135_bpt"]
		self.p_Home_TextBox140_bpt = state["p_Home_TextBox140_bpt"]
		self.p_Home_TextBox141_bpt = state["p_Home_TextBox141_bpt"]
		self.p_Home_TextBox124_bpt = state["p_Home_TextBox124_bpt"]
		self.p_Home_Image72_bpt = state["p_Home_Image72_bpt"]
		self.p_Home_Image73_bpt = state["p_Home_Image73_bpt"]
		self.p_Home_Image70_bpt = state["p_Home_Image70_bpt"]
		self.p_Home_Image71_bpt = state["p_Home_Image71_bpt"]
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	def set_event(self, event):
		self.event_data = event["event_data"]
		self.event_alias = event["alias"]
		callback_name = event["callback_name"]
		comp = getattr(self, self.event_alias)
		setattr(comp, callback_name, True)
	@property
	def p_Home_Flex1_bpt(self):
		self._getter_access_tracker["p_Home_Flex1_bpt"] = {}
		return self._p_Home_Flex1_bpt
	@p_Home_Flex1_bpt.setter
	def p_Home_Flex1_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex1_bpt"] = {}
		global default_state
		self._p_Home_Flex1_bpt = Flex(new_state, default_state["p_Home_Flex1_bpt"])

	@property
	def p_Home_Flex2_bpt(self):
		self._getter_access_tracker["p_Home_Flex2_bpt"] = {}
		return self._p_Home_Flex2_bpt
	@p_Home_Flex2_bpt.setter
	def p_Home_Flex2_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex2_bpt"] = {}
		global default_state
		self._p_Home_Flex2_bpt = Flex(new_state, default_state["p_Home_Flex2_bpt"])

	@property
	def p_Home_Flex4_bpt(self):
		self._getter_access_tracker["p_Home_Flex4_bpt"] = {}
		return self._p_Home_Flex4_bpt
	@p_Home_Flex4_bpt.setter
	def p_Home_Flex4_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex4_bpt"] = {}
		global default_state
		self._p_Home_Flex4_bpt = Flex(new_state, default_state["p_Home_Flex4_bpt"])

	@property
	def p_Home_Flex138_bpt(self):
		self._getter_access_tracker["p_Home_Flex138_bpt"] = {}
		return self._p_Home_Flex138_bpt
	@p_Home_Flex138_bpt.setter
	def p_Home_Flex138_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex138_bpt"] = {}
		global default_state
		self._p_Home_Flex138_bpt = Flex(new_state, default_state["p_Home_Flex138_bpt"])

	@property
	def p_Home_TextBox1_bpt(self):
		self._getter_access_tracker["p_Home_TextBox1_bpt"] = {}
		return self._p_Home_TextBox1_bpt
	@p_Home_TextBox1_bpt.setter
	def p_Home_TextBox1_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox1_bpt"] = {}
		global default_state
		self._p_Home_TextBox1_bpt = Div(new_state, default_state["p_Home_TextBox1_bpt"])

	@property
	def p_Home_TextBox2_bpt(self):
		self._getter_access_tracker["p_Home_TextBox2_bpt"] = {}
		return self._p_Home_TextBox2_bpt
	@p_Home_TextBox2_bpt.setter
	def p_Home_TextBox2_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox2_bpt"] = {}
		global default_state
		self._p_Home_TextBox2_bpt = Div(new_state, default_state["p_Home_TextBox2_bpt"])

	@property
	def p_Home_TextBox6_bpt(self):
		self._getter_access_tracker["p_Home_TextBox6_bpt"] = {}
		return self._p_Home_TextBox6_bpt
	@p_Home_TextBox6_bpt.setter
	def p_Home_TextBox6_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox6_bpt"] = {}
		global default_state
		self._p_Home_TextBox6_bpt = Div(new_state, default_state["p_Home_TextBox6_bpt"])

	@property
	def p_Home_TextBox4_bpt(self):
		self._getter_access_tracker["p_Home_TextBox4_bpt"] = {}
		return self._p_Home_TextBox4_bpt
	@p_Home_TextBox4_bpt.setter
	def p_Home_TextBox4_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox4_bpt"] = {}
		global default_state
		self._p_Home_TextBox4_bpt = Div(new_state, default_state["p_Home_TextBox4_bpt"])

	@property
	def p_Home_TextBox3_bpt(self):
		self._getter_access_tracker["p_Home_TextBox3_bpt"] = {}
		return self._p_Home_TextBox3_bpt
	@p_Home_TextBox3_bpt.setter
	def p_Home_TextBox3_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox3_bpt"] = {}
		global default_state
		self._p_Home_TextBox3_bpt = Div(new_state, default_state["p_Home_TextBox3_bpt"])

	@property
	def p_Home_Flex3_bpt(self):
		self._getter_access_tracker["p_Home_Flex3_bpt"] = {}
		return self._p_Home_Flex3_bpt
	@p_Home_Flex3_bpt.setter
	def p_Home_Flex3_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex3_bpt"] = {}
		global default_state
		self._p_Home_Flex3_bpt = Flex(new_state, default_state["p_Home_Flex3_bpt"])

	@property
	def p_Home_Flex5_bpt(self):
		self._getter_access_tracker["p_Home_Flex5_bpt"] = {}
		return self._p_Home_Flex5_bpt
	@p_Home_Flex5_bpt.setter
	def p_Home_Flex5_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex5_bpt"] = {}
		global default_state
		self._p_Home_Flex5_bpt = Flex(new_state, default_state["p_Home_Flex5_bpt"])

	@property
	def p_Home_Flex6_bpt(self):
		self._getter_access_tracker["p_Home_Flex6_bpt"] = {}
		return self._p_Home_Flex6_bpt
	@p_Home_Flex6_bpt.setter
	def p_Home_Flex6_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex6_bpt"] = {}
		global default_state
		self._p_Home_Flex6_bpt = Flex(new_state, default_state["p_Home_Flex6_bpt"])

	@property
	def p_Home_TextBox9_bpt(self):
		self._getter_access_tracker["p_Home_TextBox9_bpt"] = {}
		return self._p_Home_TextBox9_bpt
	@p_Home_TextBox9_bpt.setter
	def p_Home_TextBox9_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox9_bpt"] = {}
		global default_state
		self._p_Home_TextBox9_bpt = Div(new_state, default_state["p_Home_TextBox9_bpt"])

	@property
	def p_Home_Flex8_bpt(self):
		self._getter_access_tracker["p_Home_Flex8_bpt"] = {}
		return self._p_Home_Flex8_bpt
	@p_Home_Flex8_bpt.setter
	def p_Home_Flex8_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex8_bpt"] = {}
		global default_state
		self._p_Home_Flex8_bpt = Flex(new_state, default_state["p_Home_Flex8_bpt"])

	@property
	def p_Home_Flex9_bpt(self):
		self._getter_access_tracker["p_Home_Flex9_bpt"] = {}
		return self._p_Home_Flex9_bpt
	@p_Home_Flex9_bpt.setter
	def p_Home_Flex9_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex9_bpt"] = {}
		global default_state
		self._p_Home_Flex9_bpt = Flex(new_state, default_state["p_Home_Flex9_bpt"])

	@property
	def p_Home_Flex10_bpt(self):
		self._getter_access_tracker["p_Home_Flex10_bpt"] = {}
		return self._p_Home_Flex10_bpt
	@p_Home_Flex10_bpt.setter
	def p_Home_Flex10_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex10_bpt"] = {}
		global default_state
		self._p_Home_Flex10_bpt = Flex(new_state, default_state["p_Home_Flex10_bpt"])

	@property
	def p_Home_TextBox7_bpt(self):
		self._getter_access_tracker["p_Home_TextBox7_bpt"] = {}
		return self._p_Home_TextBox7_bpt
	@p_Home_TextBox7_bpt.setter
	def p_Home_TextBox7_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox7_bpt"] = {}
		global default_state
		self._p_Home_TextBox7_bpt = Div(new_state, default_state["p_Home_TextBox7_bpt"])

	@property
	def p_Home_TextBox8_bpt(self):
		self._getter_access_tracker["p_Home_TextBox8_bpt"] = {}
		return self._p_Home_TextBox8_bpt
	@p_Home_TextBox8_bpt.setter
	def p_Home_TextBox8_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox8_bpt"] = {}
		global default_state
		self._p_Home_TextBox8_bpt = Div(new_state, default_state["p_Home_TextBox8_bpt"])

	@property
	def p_Home_Flex7_bpt(self):
		self._getter_access_tracker["p_Home_Flex7_bpt"] = {}
		return self._p_Home_Flex7_bpt
	@p_Home_Flex7_bpt.setter
	def p_Home_Flex7_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex7_bpt"] = {}
		global default_state
		self._p_Home_Flex7_bpt = Flex(new_state, default_state["p_Home_Flex7_bpt"])

	@property
	def p_Home_Flex11_bpt(self):
		self._getter_access_tracker["p_Home_Flex11_bpt"] = {}
		return self._p_Home_Flex11_bpt
	@p_Home_Flex11_bpt.setter
	def p_Home_Flex11_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex11_bpt"] = {}
		global default_state
		self._p_Home_Flex11_bpt = Flex(new_state, default_state["p_Home_Flex11_bpt"])

	@property
	def p_Home_Flex12_bpt(self):
		self._getter_access_tracker["p_Home_Flex12_bpt"] = {}
		return self._p_Home_Flex12_bpt
	@p_Home_Flex12_bpt.setter
	def p_Home_Flex12_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex12_bpt"] = {}
		global default_state
		self._p_Home_Flex12_bpt = Flex(new_state, default_state["p_Home_Flex12_bpt"])

	@property
	def p_Home_Flex371_bpt(self):
		self._getter_access_tracker["p_Home_Flex371_bpt"] = {}
		return self._p_Home_Flex371_bpt
	@p_Home_Flex371_bpt.setter
	def p_Home_Flex371_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex371_bpt"] = {}
		global default_state
		self._p_Home_Flex371_bpt = Flex(new_state, default_state["p_Home_Flex371_bpt"])

	@property
	def p_Home_Flex373_bpt(self):
		self._getter_access_tracker["p_Home_Flex373_bpt"] = {}
		return self._p_Home_Flex373_bpt
	@p_Home_Flex373_bpt.setter
	def p_Home_Flex373_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex373_bpt"] = {}
		global default_state
		self._p_Home_Flex373_bpt = Flex(new_state, default_state["p_Home_Flex373_bpt"])

	@property
	def p_Home_Flex13_bpt(self):
		self._getter_access_tracker["p_Home_Flex13_bpt"] = {}
		return self._p_Home_Flex13_bpt
	@p_Home_Flex13_bpt.setter
	def p_Home_Flex13_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex13_bpt"] = {}
		global default_state
		self._p_Home_Flex13_bpt = Flex(new_state, default_state["p_Home_Flex13_bpt"])

	@property
	def p_Home_Flex14_bpt(self):
		self._getter_access_tracker["p_Home_Flex14_bpt"] = {}
		return self._p_Home_Flex14_bpt
	@p_Home_Flex14_bpt.setter
	def p_Home_Flex14_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex14_bpt"] = {}
		global default_state
		self._p_Home_Flex14_bpt = Flex(new_state, default_state["p_Home_Flex14_bpt"])

	@property
	def p_Home_Flex365_bpt(self):
		self._getter_access_tracker["p_Home_Flex365_bpt"] = {}
		return self._p_Home_Flex365_bpt
	@p_Home_Flex365_bpt.setter
	def p_Home_Flex365_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex365_bpt"] = {}
		global default_state
		self._p_Home_Flex365_bpt = Flex(new_state, default_state["p_Home_Flex365_bpt"])

	@property
	def p_Home_Flex15_bpt(self):
		self._getter_access_tracker["p_Home_Flex15_bpt"] = {}
		return self._p_Home_Flex15_bpt
	@p_Home_Flex15_bpt.setter
	def p_Home_Flex15_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex15_bpt"] = {}
		global default_state
		self._p_Home_Flex15_bpt = Flex(new_state, default_state["p_Home_Flex15_bpt"])

	@property
	def p_Home_Flex366_bpt(self):
		self._getter_access_tracker["p_Home_Flex366_bpt"] = {}
		return self._p_Home_Flex366_bpt
	@p_Home_Flex366_bpt.setter
	def p_Home_Flex366_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex366_bpt"] = {}
		global default_state
		self._p_Home_Flex366_bpt = Flex(new_state, default_state["p_Home_Flex366_bpt"])

	@property
	def p_Home_Flex367_bpt(self):
		self._getter_access_tracker["p_Home_Flex367_bpt"] = {}
		return self._p_Home_Flex367_bpt
	@p_Home_Flex367_bpt.setter
	def p_Home_Flex367_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex367_bpt"] = {}
		global default_state
		self._p_Home_Flex367_bpt = Flex(new_state, default_state["p_Home_Flex367_bpt"])

	@property
	def p_Home_Flex21_bpt(self):
		self._getter_access_tracker["p_Home_Flex21_bpt"] = {}
		return self._p_Home_Flex21_bpt
	@p_Home_Flex21_bpt.setter
	def p_Home_Flex21_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex21_bpt"] = {}
		global default_state
		self._p_Home_Flex21_bpt = Flex(new_state, default_state["p_Home_Flex21_bpt"])

	@property
	def p_Home_Flex368_bpt(self):
		self._getter_access_tracker["p_Home_Flex368_bpt"] = {}
		return self._p_Home_Flex368_bpt
	@p_Home_Flex368_bpt.setter
	def p_Home_Flex368_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex368_bpt"] = {}
		global default_state
		self._p_Home_Flex368_bpt = Flex(new_state, default_state["p_Home_Flex368_bpt"])

	@property
	def p_Home_Flex25_bpt(self):
		self._getter_access_tracker["p_Home_Flex25_bpt"] = {}
		return self._p_Home_Flex25_bpt
	@p_Home_Flex25_bpt.setter
	def p_Home_Flex25_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex25_bpt"] = {}
		global default_state
		self._p_Home_Flex25_bpt = Flex(new_state, default_state["p_Home_Flex25_bpt"])

	@property
	def p_Home_Flex26_bpt(self):
		self._getter_access_tracker["p_Home_Flex26_bpt"] = {}
		return self._p_Home_Flex26_bpt
	@p_Home_Flex26_bpt.setter
	def p_Home_Flex26_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex26_bpt"] = {}
		global default_state
		self._p_Home_Flex26_bpt = Flex(new_state, default_state["p_Home_Flex26_bpt"])

	@property
	def p_Home_Flex27_bpt(self):
		self._getter_access_tracker["p_Home_Flex27_bpt"] = {}
		return self._p_Home_Flex27_bpt
	@p_Home_Flex27_bpt.setter
	def p_Home_Flex27_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex27_bpt"] = {}
		global default_state
		self._p_Home_Flex27_bpt = Flex(new_state, default_state["p_Home_Flex27_bpt"])

	@property
	def p_Home_Flex29_bpt(self):
		self._getter_access_tracker["p_Home_Flex29_bpt"] = {}
		return self._p_Home_Flex29_bpt
	@p_Home_Flex29_bpt.setter
	def p_Home_Flex29_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex29_bpt"] = {}
		global default_state
		self._p_Home_Flex29_bpt = Flex(new_state, default_state["p_Home_Flex29_bpt"])

	@property
	def p_Home_Flex30_bpt(self):
		self._getter_access_tracker["p_Home_Flex30_bpt"] = {}
		return self._p_Home_Flex30_bpt
	@p_Home_Flex30_bpt.setter
	def p_Home_Flex30_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex30_bpt"] = {}
		global default_state
		self._p_Home_Flex30_bpt = Flex(new_state, default_state["p_Home_Flex30_bpt"])

	@property
	def p_Home_Flex35_bpt(self):
		self._getter_access_tracker["p_Home_Flex35_bpt"] = {}
		return self._p_Home_Flex35_bpt
	@p_Home_Flex35_bpt.setter
	def p_Home_Flex35_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex35_bpt"] = {}
		global default_state
		self._p_Home_Flex35_bpt = Flex(new_state, default_state["p_Home_Flex35_bpt"])

	@property
	def p_Home_Flex32_bpt(self):
		self._getter_access_tracker["p_Home_Flex32_bpt"] = {}
		return self._p_Home_Flex32_bpt
	@p_Home_Flex32_bpt.setter
	def p_Home_Flex32_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex32_bpt"] = {}
		global default_state
		self._p_Home_Flex32_bpt = Flex(new_state, default_state["p_Home_Flex32_bpt"])

	@property
	def p_Home_Flex28_bpt(self):
		self._getter_access_tracker["p_Home_Flex28_bpt"] = {}
		return self._p_Home_Flex28_bpt
	@p_Home_Flex28_bpt.setter
	def p_Home_Flex28_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex28_bpt"] = {}
		global default_state
		self._p_Home_Flex28_bpt = Flex(new_state, default_state["p_Home_Flex28_bpt"])

	@property
	def p_Home_Flex37_bpt(self):
		self._getter_access_tracker["p_Home_Flex37_bpt"] = {}
		return self._p_Home_Flex37_bpt
	@p_Home_Flex37_bpt.setter
	def p_Home_Flex37_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex37_bpt"] = {}
		global default_state
		self._p_Home_Flex37_bpt = Flex(new_state, default_state["p_Home_Flex37_bpt"])

	@property
	def p__Home_Flex38_bpt(self):
		self._getter_access_tracker["p__Home_Flex38_bpt"] = {}
		return self._p__Home_Flex38_bpt
	@p__Home_Flex38_bpt.setter
	def p__Home_Flex38_bpt(self, new_state):
		self._setter_access_tracker["p__Home_Flex38_bpt"] = {}
		global default_state
		self._p__Home_Flex38_bpt = Flex(new_state, default_state["p__Home_Flex38_bpt"])

	@property
	def p_Home_Flex39_bpt(self):
		self._getter_access_tracker["p_Home_Flex39_bpt"] = {}
		return self._p_Home_Flex39_bpt
	@p_Home_Flex39_bpt.setter
	def p_Home_Flex39_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex39_bpt"] = {}
		global default_state
		self._p_Home_Flex39_bpt = Flex(new_state, default_state["p_Home_Flex39_bpt"])

	@property
	def p_Home_Flex40_bpt(self):
		self._getter_access_tracker["p_Home_Flex40_bpt"] = {}
		return self._p_Home_Flex40_bpt
	@p_Home_Flex40_bpt.setter
	def p_Home_Flex40_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex40_bpt"] = {}
		global default_state
		self._p_Home_Flex40_bpt = Flex(new_state, default_state["p_Home_Flex40_bpt"])

	@property
	def p_Home_Flex297_bpt(self):
		self._getter_access_tracker["p_Home_Flex297_bpt"] = {}
		return self._p_Home_Flex297_bpt
	@p_Home_Flex297_bpt.setter
	def p_Home_Flex297_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex297_bpt"] = {}
		global default_state
		self._p_Home_Flex297_bpt = Flex(new_state, default_state["p_Home_Flex297_bpt"])

	@property
	def p_Home_Product_Card_1_bpt(self):
		self._getter_access_tracker["p_Home_Product_Card_1_bpt"] = {}
		return self._p_Home_Product_Card_1_bpt
	@p_Home_Product_Card_1_bpt.setter
	def p_Home_Product_Card_1_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Card_1_bpt"] = {}
		global default_state
		self._p_Home_Product_Card_1_bpt = Flex(new_state, default_state["p_Home_Product_Card_1_bpt"])

	@property
	def p_Home_Flex42_bpt(self):
		self._getter_access_tracker["p_Home_Flex42_bpt"] = {}
		return self._p_Home_Flex42_bpt
	@p_Home_Flex42_bpt.setter
	def p_Home_Flex42_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex42_bpt"] = {}
		global default_state
		self._p_Home_Flex42_bpt = Flex(new_state, default_state["p_Home_Flex42_bpt"])

	@property
	def p_Home_Product_Card_2_bpt(self):
		self._getter_access_tracker["p_Home_Product_Card_2_bpt"] = {}
		return self._p_Home_Product_Card_2_bpt
	@p_Home_Product_Card_2_bpt.setter
	def p_Home_Product_Card_2_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Card_2_bpt"] = {}
		global default_state
		self._p_Home_Product_Card_2_bpt = Flex(new_state, default_state["p_Home_Product_Card_2_bpt"])

	@property
	def p_Home_Flex43_bpt(self):
		self._getter_access_tracker["p_Home_Flex43_bpt"] = {}
		return self._p_Home_Flex43_bpt
	@p_Home_Flex43_bpt.setter
	def p_Home_Flex43_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex43_bpt"] = {}
		global default_state
		self._p_Home_Flex43_bpt = Flex(new_state, default_state["p_Home_Flex43_bpt"])

	@property
	def p_Home_Flex298_bpt(self):
		self._getter_access_tracker["p_Home_Flex298_bpt"] = {}
		return self._p_Home_Flex298_bpt
	@p_Home_Flex298_bpt.setter
	def p_Home_Flex298_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex298_bpt"] = {}
		global default_state
		self._p_Home_Flex298_bpt = Flex(new_state, default_state["p_Home_Flex298_bpt"])

	@property
	def p_Home_Product_Card_4_bpt(self):
		self._getter_access_tracker["p_Home_Product_Card_4_bpt"] = {}
		return self._p_Home_Product_Card_4_bpt
	@p_Home_Product_Card_4_bpt.setter
	def p_Home_Product_Card_4_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Card_4_bpt"] = {}
		global default_state
		self._p_Home_Product_Card_4_bpt = Flex(new_state, default_state["p_Home_Product_Card_4_bpt"])

	@property
	def p_Home_Flex47_bpt(self):
		self._getter_access_tracker["p_Home_Flex47_bpt"] = {}
		return self._p_Home_Flex47_bpt
	@p_Home_Flex47_bpt.setter
	def p_Home_Flex47_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex47_bpt"] = {}
		global default_state
		self._p_Home_Flex47_bpt = Flex(new_state, default_state["p_Home_Flex47_bpt"])

	@property
	def p_Home_Product_Card_3_bpt(self):
		self._getter_access_tracker["p_Home_Product_Card_3_bpt"] = {}
		return self._p_Home_Product_Card_3_bpt
	@p_Home_Product_Card_3_bpt.setter
	def p_Home_Product_Card_3_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Card_3_bpt"] = {}
		global default_state
		self._p_Home_Product_Card_3_bpt = Flex(new_state, default_state["p_Home_Product_Card_3_bpt"])

	@property
	def p_Home_Flex45_bpt(self):
		self._getter_access_tracker["p_Home_Flex45_bpt"] = {}
		return self._p_Home_Flex45_bpt
	@p_Home_Flex45_bpt.setter
	def p_Home_Flex45_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex45_bpt"] = {}
		global default_state
		self._p_Home_Flex45_bpt = Flex(new_state, default_state["p_Home_Flex45_bpt"])

	@property
	def p_Home_Flex58_bpt(self):
		self._getter_access_tracker["p_Home_Flex58_bpt"] = {}
		return self._p_Home_Flex58_bpt
	@p_Home_Flex58_bpt.setter
	def p_Home_Flex58_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex58_bpt"] = {}
		global default_state
		self._p_Home_Flex58_bpt = Flex(new_state, default_state["p_Home_Flex58_bpt"])

	@property
	def p_Home_Flex57_bpt(self):
		self._getter_access_tracker["p_Home_Flex57_bpt"] = {}
		return self._p_Home_Flex57_bpt
	@p_Home_Flex57_bpt.setter
	def p_Home_Flex57_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex57_bpt"] = {}
		global default_state
		self._p_Home_Flex57_bpt = Flex(new_state, default_state["p_Home_Flex57_bpt"])

	@property
	def p_Home_Flex300_bpt(self):
		self._getter_access_tracker["p_Home_Flex300_bpt"] = {}
		return self._p_Home_Flex300_bpt
	@p_Home_Flex300_bpt.setter
	def p_Home_Flex300_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex300_bpt"] = {}
		global default_state
		self._p_Home_Flex300_bpt = Flex(new_state, default_state["p_Home_Flex300_bpt"])

	@property
	def p_Home_Product_Card_7_bpt(self):
		self._getter_access_tracker["p_Home_Product_Card_7_bpt"] = {}
		return self._p_Home_Product_Card_7_bpt
	@p_Home_Product_Card_7_bpt.setter
	def p_Home_Product_Card_7_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Card_7_bpt"] = {}
		global default_state
		self._p_Home_Product_Card_7_bpt = Flex(new_state, default_state["p_Home_Product_Card_7_bpt"])

	@property
	def p_Home_Flex50_bpt(self):
		self._getter_access_tracker["p_Home_Flex50_bpt"] = {}
		return self._p_Home_Flex50_bpt
	@p_Home_Flex50_bpt.setter
	def p_Home_Flex50_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex50_bpt"] = {}
		global default_state
		self._p_Home_Flex50_bpt = Flex(new_state, default_state["p_Home_Flex50_bpt"])

	@property
	def p_Home_Product_Card_8_bpt(self):
		self._getter_access_tracker["p_Home_Product_Card_8_bpt"] = {}
		return self._p_Home_Product_Card_8_bpt
	@p_Home_Product_Card_8_bpt.setter
	def p_Home_Product_Card_8_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Card_8_bpt"] = {}
		global default_state
		self._p_Home_Product_Card_8_bpt = Flex(new_state, default_state["p_Home_Product_Card_8_bpt"])

	@property
	def p_Home_Flex49_bpt(self):
		self._getter_access_tracker["p_Home_Flex49_bpt"] = {}
		return self._p_Home_Flex49_bpt
	@p_Home_Flex49_bpt.setter
	def p_Home_Flex49_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex49_bpt"] = {}
		global default_state
		self._p_Home_Flex49_bpt = Flex(new_state, default_state["p_Home_Flex49_bpt"])

	@property
	def p_Home_Flex299_bpt(self):
		self._getter_access_tracker["p_Home_Flex299_bpt"] = {}
		return self._p_Home_Flex299_bpt
	@p_Home_Flex299_bpt.setter
	def p_Home_Flex299_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex299_bpt"] = {}
		global default_state
		self._p_Home_Flex299_bpt = Flex(new_state, default_state["p_Home_Flex299_bpt"])

	@property
	def p_Home_Product_Card_6_bpt(self):
		self._getter_access_tracker["p_Home_Product_Card_6_bpt"] = {}
		return self._p_Home_Product_Card_6_bpt
	@p_Home_Product_Card_6_bpt.setter
	def p_Home_Product_Card_6_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Card_6_bpt"] = {}
		global default_state
		self._p_Home_Product_Card_6_bpt = Flex(new_state, default_state["p_Home_Product_Card_6_bpt"])

	@property
	def p_Home_Flex51_bpt(self):
		self._getter_access_tracker["p_Home_Flex51_bpt"] = {}
		return self._p_Home_Flex51_bpt
	@p_Home_Flex51_bpt.setter
	def p_Home_Flex51_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex51_bpt"] = {}
		global default_state
		self._p_Home_Flex51_bpt = Flex(new_state, default_state["p_Home_Flex51_bpt"])

	@property
	def p_Home_Product_Card_5_bpt(self):
		self._getter_access_tracker["p_Home_Product_Card_5_bpt"] = {}
		return self._p_Home_Product_Card_5_bpt
	@p_Home_Product_Card_5_bpt.setter
	def p_Home_Product_Card_5_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Card_5_bpt"] = {}
		global default_state
		self._p_Home_Product_Card_5_bpt = Flex(new_state, default_state["p_Home_Product_Card_5_bpt"])

	@property
	def p_Home_Flex52_bpt(self):
		self._getter_access_tracker["p_Home_Flex52_bpt"] = {}
		return self._p_Home_Flex52_bpt
	@p_Home_Flex52_bpt.setter
	def p_Home_Flex52_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex52_bpt"] = {}
		global default_state
		self._p_Home_Flex52_bpt = Flex(new_state, default_state["p_Home_Flex52_bpt"])

	@property
	def p_Home_Flex59_bpt(self):
		self._getter_access_tracker["p_Home_Flex59_bpt"] = {}
		return self._p_Home_Flex59_bpt
	@p_Home_Flex59_bpt.setter
	def p_Home_Flex59_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex59_bpt"] = {}
		global default_state
		self._p_Home_Flex59_bpt = Flex(new_state, default_state["p_Home_Flex59_bpt"])

	@property
	def p_Home_Flex60_bpt(self):
		self._getter_access_tracker["p_Home_Flex60_bpt"] = {}
		return self._p_Home_Flex60_bpt
	@p_Home_Flex60_bpt.setter
	def p_Home_Flex60_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex60_bpt"] = {}
		global default_state
		self._p_Home_Flex60_bpt = Flex(new_state, default_state["p_Home_Flex60_bpt"])

	@property
	def p_Home_Flex62_bpt(self):
		self._getter_access_tracker["p_Home_Flex62_bpt"] = {}
		return self._p_Home_Flex62_bpt
	@p_Home_Flex62_bpt.setter
	def p_Home_Flex62_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex62_bpt"] = {}
		global default_state
		self._p_Home_Flex62_bpt = Flex(new_state, default_state["p_Home_Flex62_bpt"])

	@property
	def p_Home_Flex61_bpt(self):
		self._getter_access_tracker["p_Home_Flex61_bpt"] = {}
		return self._p_Home_Flex61_bpt
	@p_Home_Flex61_bpt.setter
	def p_Home_Flex61_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex61_bpt"] = {}
		global default_state
		self._p_Home_Flex61_bpt = Flex(new_state, default_state["p_Home_Flex61_bpt"])

	@property
	def p_Home_Flex63_bpt(self):
		self._getter_access_tracker["p_Home_Flex63_bpt"] = {}
		return self._p_Home_Flex63_bpt
	@p_Home_Flex63_bpt.setter
	def p_Home_Flex63_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex63_bpt"] = {}
		global default_state
		self._p_Home_Flex63_bpt = Flex(new_state, default_state["p_Home_Flex63_bpt"])

	@property
	def p_Home_Flex130_bpt(self):
		self._getter_access_tracker["p_Home_Flex130_bpt"] = {}
		return self._p_Home_Flex130_bpt
	@p_Home_Flex130_bpt.setter
	def p_Home_Flex130_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex130_bpt"] = {}
		global default_state
		self._p_Home_Flex130_bpt = Flex(new_state, default_state["p_Home_Flex130_bpt"])

	@property
	def p_Home_Flex89_bpt(self):
		self._getter_access_tracker["p_Home_Flex89_bpt"] = {}
		return self._p_Home_Flex89_bpt
	@p_Home_Flex89_bpt.setter
	def p_Home_Flex89_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex89_bpt"] = {}
		global default_state
		self._p_Home_Flex89_bpt = Flex(new_state, default_state["p_Home_Flex89_bpt"])

	@property
	def p_Home_Flex128_bpt(self):
		self._getter_access_tracker["p_Home_Flex128_bpt"] = {}
		return self._p_Home_Flex128_bpt
	@p_Home_Flex128_bpt.setter
	def p_Home_Flex128_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex128_bpt"] = {}
		global default_state
		self._p_Home_Flex128_bpt = Flex(new_state, default_state["p_Home_Flex128_bpt"])

	@property
	def p_Home_Flex64_bpt(self):
		self._getter_access_tracker["p_Home_Flex64_bpt"] = {}
		return self._p_Home_Flex64_bpt
	@p_Home_Flex64_bpt.setter
	def p_Home_Flex64_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex64_bpt"] = {}
		global default_state
		self._p_Home_Flex64_bpt = Flex(new_state, default_state["p_Home_Flex64_bpt"])

	@property
	def p_Home_Flex65_bpt(self):
		self._getter_access_tracker["p_Home_Flex65_bpt"] = {}
		return self._p_Home_Flex65_bpt
	@p_Home_Flex65_bpt.setter
	def p_Home_Flex65_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex65_bpt"] = {}
		global default_state
		self._p_Home_Flex65_bpt = Flex(new_state, default_state["p_Home_Flex65_bpt"])

	@property
	def p_Home_Flex131_bpt(self):
		self._getter_access_tracker["p_Home_Flex131_bpt"] = {}
		return self._p_Home_Flex131_bpt
	@p_Home_Flex131_bpt.setter
	def p_Home_Flex131_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex131_bpt"] = {}
		global default_state
		self._p_Home_Flex131_bpt = Flex(new_state, default_state["p_Home_Flex131_bpt"])

	@property
	def p_Home_Flex132_bpt(self):
		self._getter_access_tracker["p_Home_Flex132_bpt"] = {}
		return self._p_Home_Flex132_bpt
	@p_Home_Flex132_bpt.setter
	def p_Home_Flex132_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex132_bpt"] = {}
		global default_state
		self._p_Home_Flex132_bpt = Flex(new_state, default_state["p_Home_Flex132_bpt"])

	@property
	def p_Home_Flex133_bpt(self):
		self._getter_access_tracker["p_Home_Flex133_bpt"] = {}
		return self._p_Home_Flex133_bpt
	@p_Home_Flex133_bpt.setter
	def p_Home_Flex133_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex133_bpt"] = {}
		global default_state
		self._p_Home_Flex133_bpt = Flex(new_state, default_state["p_Home_Flex133_bpt"])

	@property
	def p_Home_Flex134_bpt(self):
		self._getter_access_tracker["p_Home_Flex134_bpt"] = {}
		return self._p_Home_Flex134_bpt
	@p_Home_Flex134_bpt.setter
	def p_Home_Flex134_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex134_bpt"] = {}
		global default_state
		self._p_Home_Flex134_bpt = Flex(new_state, default_state["p_Home_Flex134_bpt"])

	@property
	def p_Home_Flex1315_bpt(self):
		self._getter_access_tracker["p_Home_Flex1315_bpt"] = {}
		return self._p_Home_Flex1315_bpt
	@p_Home_Flex1315_bpt.setter
	def p_Home_Flex1315_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex1315_bpt"] = {}
		global default_state
		self._p_Home_Flex1315_bpt = Flex(new_state, default_state["p_Home_Flex1315_bpt"])

	@property
	def p_Home_Flex67_bpt(self):
		self._getter_access_tracker["p_Home_Flex67_bpt"] = {}
		return self._p_Home_Flex67_bpt
	@p_Home_Flex67_bpt.setter
	def p_Home_Flex67_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex67_bpt"] = {}
		global default_state
		self._p_Home_Flex67_bpt = Flex(new_state, default_state["p_Home_Flex67_bpt"])

	@property
	def p_Home_Flex68_bpt(self):
		self._getter_access_tracker["p_Home_Flex68_bpt"] = {}
		return self._p_Home_Flex68_bpt
	@p_Home_Flex68_bpt.setter
	def p_Home_Flex68_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex68_bpt"] = {}
		global default_state
		self._p_Home_Flex68_bpt = Flex(new_state, default_state["p_Home_Flex68_bpt"])

	@property
	def p_Home_Flex129_bpt(self):
		self._getter_access_tracker["p_Home_Flex129_bpt"] = {}
		return self._p_Home_Flex129_bpt
	@p_Home_Flex129_bpt.setter
	def p_Home_Flex129_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex129_bpt"] = {}
		global default_state
		self._p_Home_Flex129_bpt = Flex(new_state, default_state["p_Home_Flex129_bpt"])

	@property
	def p_Home_Flex69_bpt(self):
		self._getter_access_tracker["p_Home_Flex69_bpt"] = {}
		return self._p_Home_Flex69_bpt
	@p_Home_Flex69_bpt.setter
	def p_Home_Flex69_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex69_bpt"] = {}
		global default_state
		self._p_Home_Flex69_bpt = Flex(new_state, default_state["p_Home_Flex69_bpt"])

	@property
	def p_Home_Flex71_bpt(self):
		self._getter_access_tracker["p_Home_Flex71_bpt"] = {}
		return self._p_Home_Flex71_bpt
	@p_Home_Flex71_bpt.setter
	def p_Home_Flex71_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex71_bpt"] = {}
		global default_state
		self._p_Home_Flex71_bpt = Flex(new_state, default_state["p_Home_Flex71_bpt"])

	@property
	def p_Home_Flex72_bpt(self):
		self._getter_access_tracker["p_Home_Flex72_bpt"] = {}
		return self._p_Home_Flex72_bpt
	@p_Home_Flex72_bpt.setter
	def p_Home_Flex72_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex72_bpt"] = {}
		global default_state
		self._p_Home_Flex72_bpt = Flex(new_state, default_state["p_Home_Flex72_bpt"])

	@property
	def p_Home_Flex73_bpt(self):
		self._getter_access_tracker["p_Home_Flex73_bpt"] = {}
		return self._p_Home_Flex73_bpt
	@p_Home_Flex73_bpt.setter
	def p_Home_Flex73_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex73_bpt"] = {}
		global default_state
		self._p_Home_Flex73_bpt = Flex(new_state, default_state["p_Home_Flex73_bpt"])

	@property
	def p_Home_Flex74_bpt(self):
		self._getter_access_tracker["p_Home_Flex74_bpt"] = {}
		return self._p_Home_Flex74_bpt
	@p_Home_Flex74_bpt.setter
	def p_Home_Flex74_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex74_bpt"] = {}
		global default_state
		self._p_Home_Flex74_bpt = Flex(new_state, default_state["p_Home_Flex74_bpt"])

	@property
	def p_Home_Flex75_bpt(self):
		self._getter_access_tracker["p_Home_Flex75_bpt"] = {}
		return self._p_Home_Flex75_bpt
	@p_Home_Flex75_bpt.setter
	def p_Home_Flex75_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex75_bpt"] = {}
		global default_state
		self._p_Home_Flex75_bpt = Flex(new_state, default_state["p_Home_Flex75_bpt"])

	@property
	def p_Home_Flex76_bpt(self):
		self._getter_access_tracker["p_Home_Flex76_bpt"] = {}
		return self._p_Home_Flex76_bpt
	@p_Home_Flex76_bpt.setter
	def p_Home_Flex76_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex76_bpt"] = {}
		global default_state
		self._p_Home_Flex76_bpt = Flex(new_state, default_state["p_Home_Flex76_bpt"])

	@property
	def p_Home_Flex77_bpt(self):
		self._getter_access_tracker["p_Home_Flex77_bpt"] = {}
		return self._p_Home_Flex77_bpt
	@p_Home_Flex77_bpt.setter
	def p_Home_Flex77_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex77_bpt"] = {}
		global default_state
		self._p_Home_Flex77_bpt = Flex(new_state, default_state["p_Home_Flex77_bpt"])

	@property
	def p_Home_Flex81_bpt(self):
		self._getter_access_tracker["p_Home_Flex81_bpt"] = {}
		return self._p_Home_Flex81_bpt
	@p_Home_Flex81_bpt.setter
	def p_Home_Flex81_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex81_bpt"] = {}
		global default_state
		self._p_Home_Flex81_bpt = Flex(new_state, default_state["p_Home_Flex81_bpt"])

	@property
	def p_Home_Flex82_bpt(self):
		self._getter_access_tracker["p_Home_Flex82_bpt"] = {}
		return self._p_Home_Flex82_bpt
	@p_Home_Flex82_bpt.setter
	def p_Home_Flex82_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex82_bpt"] = {}
		global default_state
		self._p_Home_Flex82_bpt = Flex(new_state, default_state["p_Home_Flex82_bpt"])

	@property
	def p_Home_Flex85_bpt(self):
		self._getter_access_tracker["p_Home_Flex85_bpt"] = {}
		return self._p_Home_Flex85_bpt
	@p_Home_Flex85_bpt.setter
	def p_Home_Flex85_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex85_bpt"] = {}
		global default_state
		self._p_Home_Flex85_bpt = Flex(new_state, default_state["p_Home_Flex85_bpt"])

	@property
	def p_Home_Flex83_bpt(self):
		self._getter_access_tracker["p_Home_Flex83_bpt"] = {}
		return self._p_Home_Flex83_bpt
	@p_Home_Flex83_bpt.setter
	def p_Home_Flex83_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex83_bpt"] = {}
		global default_state
		self._p_Home_Flex83_bpt = Flex(new_state, default_state["p_Home_Flex83_bpt"])

	@property
	def p_Home_Flex84_bpt(self):
		self._getter_access_tracker["p_Home_Flex84_bpt"] = {}
		return self._p_Home_Flex84_bpt
	@p_Home_Flex84_bpt.setter
	def p_Home_Flex84_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex84_bpt"] = {}
		global default_state
		self._p_Home_Flex84_bpt = Flex(new_state, default_state["p_Home_Flex84_bpt"])

	@property
	def p_Home_Flex90_bpt(self):
		self._getter_access_tracker["p_Home_Flex90_bpt"] = {}
		return self._p_Home_Flex90_bpt
	@p_Home_Flex90_bpt.setter
	def p_Home_Flex90_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex90_bpt"] = {}
		global default_state
		self._p_Home_Flex90_bpt = Flex(new_state, default_state["p_Home_Flex90_bpt"])

	@property
	def p_Home_Flex92_bpt(self):
		self._getter_access_tracker["p_Home_Flex92_bpt"] = {}
		return self._p_Home_Flex92_bpt
	@p_Home_Flex92_bpt.setter
	def p_Home_Flex92_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex92_bpt"] = {}
		global default_state
		self._p_Home_Flex92_bpt = Flex(new_state, default_state["p_Home_Flex92_bpt"])

	@property
	def p_Home_Flex98_bpt(self):
		self._getter_access_tracker["p_Home_Flex98_bpt"] = {}
		return self._p_Home_Flex98_bpt
	@p_Home_Flex98_bpt.setter
	def p_Home_Flex98_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex98_bpt"] = {}
		global default_state
		self._p_Home_Flex98_bpt = Flex(new_state, default_state["p_Home_Flex98_bpt"])

	@property
	def p_Home_Flex99_bpt(self):
		self._getter_access_tracker["p_Home_Flex99_bpt"] = {}
		return self._p_Home_Flex99_bpt
	@p_Home_Flex99_bpt.setter
	def p_Home_Flex99_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex99_bpt"] = {}
		global default_state
		self._p_Home_Flex99_bpt = Flex(new_state, default_state["p_Home_Flex99_bpt"])

	@property
	def p_Home_Flex100_bpt(self):
		self._getter_access_tracker["p_Home_Flex100_bpt"] = {}
		return self._p_Home_Flex100_bpt
	@p_Home_Flex100_bpt.setter
	def p_Home_Flex100_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex100_bpt"] = {}
		global default_state
		self._p_Home_Flex100_bpt = Flex(new_state, default_state["p_Home_Flex100_bpt"])

	@property
	def p_Home_Flex101_bpt(self):
		self._getter_access_tracker["p_Home_Flex101_bpt"] = {}
		return self._p_Home_Flex101_bpt
	@p_Home_Flex101_bpt.setter
	def p_Home_Flex101_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex101_bpt"] = {}
		global default_state
		self._p_Home_Flex101_bpt = Flex(new_state, default_state["p_Home_Flex101_bpt"])

	@property
	def p_Home_Flex104_bpt(self):
		self._getter_access_tracker["p_Home_Flex104_bpt"] = {}
		return self._p_Home_Flex104_bpt
	@p_Home_Flex104_bpt.setter
	def p_Home_Flex104_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex104_bpt"] = {}
		global default_state
		self._p_Home_Flex104_bpt = Flex(new_state, default_state["p_Home_Flex104_bpt"])

	@property
	def p_Home_Flex103_bpt(self):
		self._getter_access_tracker["p_Home_Flex103_bpt"] = {}
		return self._p_Home_Flex103_bpt
	@p_Home_Flex103_bpt.setter
	def p_Home_Flex103_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex103_bpt"] = {}
		global default_state
		self._p_Home_Flex103_bpt = Flex(new_state, default_state["p_Home_Flex103_bpt"])

	@property
	def p_Home_Flex102_bpt(self):
		self._getter_access_tracker["p_Home_Flex102_bpt"] = {}
		return self._p_Home_Flex102_bpt
	@p_Home_Flex102_bpt.setter
	def p_Home_Flex102_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex102_bpt"] = {}
		global default_state
		self._p_Home_Flex102_bpt = Flex(new_state, default_state["p_Home_Flex102_bpt"])

	@property
	def p_Home_Flex107_bpt(self):
		self._getter_access_tracker["p_Home_Flex107_bpt"] = {}
		return self._p_Home_Flex107_bpt
	@p_Home_Flex107_bpt.setter
	def p_Home_Flex107_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex107_bpt"] = {}
		global default_state
		self._p_Home_Flex107_bpt = Flex(new_state, default_state["p_Home_Flex107_bpt"])

	@property
	def p_Home_Flex106_bpt(self):
		self._getter_access_tracker["p_Home_Flex106_bpt"] = {}
		return self._p_Home_Flex106_bpt
	@p_Home_Flex106_bpt.setter
	def p_Home_Flex106_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex106_bpt"] = {}
		global default_state
		self._p_Home_Flex106_bpt = Flex(new_state, default_state["p_Home_Flex106_bpt"])

	@property
	def p_Home_Flex105_bpt(self):
		self._getter_access_tracker["p_Home_Flex105_bpt"] = {}
		return self._p_Home_Flex105_bpt
	@p_Home_Flex105_bpt.setter
	def p_Home_Flex105_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex105_bpt"] = {}
		global default_state
		self._p_Home_Flex105_bpt = Flex(new_state, default_state["p_Home_Flex105_bpt"])

	@property
	def p_Home_Flex108_bpt(self):
		self._getter_access_tracker["p_Home_Flex108_bpt"] = {}
		return self._p_Home_Flex108_bpt
	@p_Home_Flex108_bpt.setter
	def p_Home_Flex108_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex108_bpt"] = {}
		global default_state
		self._p_Home_Flex108_bpt = Flex(new_state, default_state["p_Home_Flex108_bpt"])

	@property
	def p_Home_Flex91_bpt(self):
		self._getter_access_tracker["p_Home_Flex91_bpt"] = {}
		return self._p_Home_Flex91_bpt
	@p_Home_Flex91_bpt.setter
	def p_Home_Flex91_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex91_bpt"] = {}
		global default_state
		self._p_Home_Flex91_bpt = Flex(new_state, default_state["p_Home_Flex91_bpt"])

	@property
	def p_Home_Flex93_bpt(self):
		self._getter_access_tracker["p_Home_Flex93_bpt"] = {}
		return self._p_Home_Flex93_bpt
	@p_Home_Flex93_bpt.setter
	def p_Home_Flex93_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex93_bpt"] = {}
		global default_state
		self._p_Home_Flex93_bpt = Flex(new_state, default_state["p_Home_Flex93_bpt"])

	@property
	def p_Home_Flex94_bpt(self):
		self._getter_access_tracker["p_Home_Flex94_bpt"] = {}
		return self._p_Home_Flex94_bpt
	@p_Home_Flex94_bpt.setter
	def p_Home_Flex94_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex94_bpt"] = {}
		global default_state
		self._p_Home_Flex94_bpt = Flex(new_state, default_state["p_Home_Flex94_bpt"])

	@property
	def p_Home_Flex95_bpt(self):
		self._getter_access_tracker["p_Home_Flex95_bpt"] = {}
		return self._p_Home_Flex95_bpt
	@p_Home_Flex95_bpt.setter
	def p_Home_Flex95_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex95_bpt"] = {}
		global default_state
		self._p_Home_Flex95_bpt = Flex(new_state, default_state["p_Home_Flex95_bpt"])

	@property
	def p_Home_Flex110_bpt(self):
		self._getter_access_tracker["p_Home_Flex110_bpt"] = {}
		return self._p_Home_Flex110_bpt
	@p_Home_Flex110_bpt.setter
	def p_Home_Flex110_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex110_bpt"] = {}
		global default_state
		self._p_Home_Flex110_bpt = Flex(new_state, default_state["p_Home_Flex110_bpt"])

	@property
	def p_Home_Flex112_bpt(self):
		self._getter_access_tracker["p_Home_Flex112_bpt"] = {}
		return self._p_Home_Flex112_bpt
	@p_Home_Flex112_bpt.setter
	def p_Home_Flex112_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex112_bpt"] = {}
		global default_state
		self._p_Home_Flex112_bpt = Flex(new_state, default_state["p_Home_Flex112_bpt"])

	@property
	def p_Home_Flex111_bpt(self):
		self._getter_access_tracker["p_Home_Flex111_bpt"] = {}
		return self._p_Home_Flex111_bpt
	@p_Home_Flex111_bpt.setter
	def p_Home_Flex111_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex111_bpt"] = {}
		global default_state
		self._p_Home_Flex111_bpt = Flex(new_state, default_state["p_Home_Flex111_bpt"])

	@property
	def p_Home_Flex113_bpt(self):
		self._getter_access_tracker["p_Home_Flex113_bpt"] = {}
		return self._p_Home_Flex113_bpt
	@p_Home_Flex113_bpt.setter
	def p_Home_Flex113_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex113_bpt"] = {}
		global default_state
		self._p_Home_Flex113_bpt = Flex(new_state, default_state["p_Home_Flex113_bpt"])

	@property
	def p_Home_Flex114_bpt(self):
		self._getter_access_tracker["p_Home_Flex114_bpt"] = {}
		return self._p_Home_Flex114_bpt
	@p_Home_Flex114_bpt.setter
	def p_Home_Flex114_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex114_bpt"] = {}
		global default_state
		self._p_Home_Flex114_bpt = Flex(new_state, default_state["p_Home_Flex114_bpt"])

	@property
	def p_Home_Flex115_bpt(self):
		self._getter_access_tracker["p_Home_Flex115_bpt"] = {}
		return self._p_Home_Flex115_bpt
	@p_Home_Flex115_bpt.setter
	def p_Home_Flex115_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex115_bpt"] = {}
		global default_state
		self._p_Home_Flex115_bpt = Flex(new_state, default_state["p_Home_Flex115_bpt"])

	@property
	def p_Home_Flex116_bpt(self):
		self._getter_access_tracker["p_Home_Flex116_bpt"] = {}
		return self._p_Home_Flex116_bpt
	@p_Home_Flex116_bpt.setter
	def p_Home_Flex116_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex116_bpt"] = {}
		global default_state
		self._p_Home_Flex116_bpt = Flex(new_state, default_state["p_Home_Flex116_bpt"])

	@property
	def p_Home_Flex117_bpt(self):
		self._getter_access_tracker["p_Home_Flex117_bpt"] = {}
		return self._p_Home_Flex117_bpt
	@p_Home_Flex117_bpt.setter
	def p_Home_Flex117_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex117_bpt"] = {}
		global default_state
		self._p_Home_Flex117_bpt = Flex(new_state, default_state["p_Home_Flex117_bpt"])

	@property
	def p_Home_Flex118_bpt(self):
		self._getter_access_tracker["p_Home_Flex118_bpt"] = {}
		return self._p_Home_Flex118_bpt
	@p_Home_Flex118_bpt.setter
	def p_Home_Flex118_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex118_bpt"] = {}
		global default_state
		self._p_Home_Flex118_bpt = Flex(new_state, default_state["p_Home_Flex118_bpt"])

	@property
	def p_Home_Flex121_bpt(self):
		self._getter_access_tracker["p_Home_Flex121_bpt"] = {}
		return self._p_Home_Flex121_bpt
	@p_Home_Flex121_bpt.setter
	def p_Home_Flex121_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex121_bpt"] = {}
		global default_state
		self._p_Home_Flex121_bpt = Flex(new_state, default_state["p_Home_Flex121_bpt"])

	@property
	def p_Home_Flex119_bpt(self):
		self._getter_access_tracker["p_Home_Flex119_bpt"] = {}
		return self._p_Home_Flex119_bpt
	@p_Home_Flex119_bpt.setter
	def p_Home_Flex119_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex119_bpt"] = {}
		global default_state
		self._p_Home_Flex119_bpt = Flex(new_state, default_state["p_Home_Flex119_bpt"])

	@property
	def p_Home_Flex125_bpt(self):
		self._getter_access_tracker["p_Home_Flex125_bpt"] = {}
		return self._p_Home_Flex125_bpt
	@p_Home_Flex125_bpt.setter
	def p_Home_Flex125_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex125_bpt"] = {}
		global default_state
		self._p_Home_Flex125_bpt = Flex(new_state, default_state["p_Home_Flex125_bpt"])

	@property
	def p_Home_Flex127_bpt(self):
		self._getter_access_tracker["p_Home_Flex127_bpt"] = {}
		return self._p_Home_Flex127_bpt
	@p_Home_Flex127_bpt.setter
	def p_Home_Flex127_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex127_bpt"] = {}
		global default_state
		self._p_Home_Flex127_bpt = Flex(new_state, default_state["p_Home_Flex127_bpt"])

	@property
	def p_Home_Flex120_bpt(self):
		self._getter_access_tracker["p_Home_Flex120_bpt"] = {}
		return self._p_Home_Flex120_bpt
	@p_Home_Flex120_bpt.setter
	def p_Home_Flex120_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex120_bpt"] = {}
		global default_state
		self._p_Home_Flex120_bpt = Flex(new_state, default_state["p_Home_Flex120_bpt"])

	@property
	def p_Home_Flex124_bpt(self):
		self._getter_access_tracker["p_Home_Flex124_bpt"] = {}
		return self._p_Home_Flex124_bpt
	@p_Home_Flex124_bpt.setter
	def p_Home_Flex124_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex124_bpt"] = {}
		global default_state
		self._p_Home_Flex124_bpt = Flex(new_state, default_state["p_Home_Flex124_bpt"])

	@property
	def p_Home_Flex123_bpt(self):
		self._getter_access_tracker["p_Home_Flex123_bpt"] = {}
		return self._p_Home_Flex123_bpt
	@p_Home_Flex123_bpt.setter
	def p_Home_Flex123_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex123_bpt"] = {}
		global default_state
		self._p_Home_Flex123_bpt = Flex(new_state, default_state["p_Home_Flex123_bpt"])

	@property
	def p_Home_Flex122_bpt(self):
		self._getter_access_tracker["p_Home_Flex122_bpt"] = {}
		return self._p_Home_Flex122_bpt
	@p_Home_Flex122_bpt.setter
	def p_Home_Flex122_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Flex122_bpt"] = {}
		global default_state
		self._p_Home_Flex122_bpt = Flex(new_state, default_state["p_Home_Flex122_bpt"])

	@property
	def p_Home_Image2_bpt(self):
		self._getter_access_tracker["p_Home_Image2_bpt"] = {}
		return self._p_Home_Image2_bpt
	@p_Home_Image2_bpt.setter
	def p_Home_Image2_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image2_bpt"] = {}
		global default_state
		self._p_Home_Image2_bpt = Image(new_state, default_state["p_Home_Image2_bpt"])

	@property
	def TextBox4(self):
		self._getter_access_tracker["TextBox4"] = {}
		return self._TextBox4
	@TextBox4.setter
	def TextBox4(self, new_state):
		self._setter_access_tracker["TextBox4"] = {}
		global default_state
		self._TextBox4 = TextBox(new_state, default_state["TextBox4"])

	@property
	def TextBox5(self):
		self._getter_access_tracker["TextBox5"] = {}
		return self._TextBox5
	@TextBox5.setter
	def TextBox5(self, new_state):
		self._setter_access_tracker["TextBox5"] = {}
		global default_state
		self._TextBox5 = TextBox(new_state, default_state["TextBox5"])

	@property
	def TextBox8(self):
		self._getter_access_tracker["TextBox8"] = {}
		return self._TextBox8
	@TextBox8.setter
	def TextBox8(self, new_state):
		self._setter_access_tracker["TextBox8"] = {}
		global default_state
		self._TextBox8 = TextBox(new_state, default_state["TextBox8"])

	@property
	def TextBox7(self):
		self._getter_access_tracker["TextBox7"] = {}
		return self._TextBox7
	@TextBox7.setter
	def TextBox7(self, new_state):
		self._setter_access_tracker["TextBox7"] = {}
		global default_state
		self._TextBox7 = TextBox(new_state, default_state["TextBox7"])

	@property
	def TextBox6(self):
		self._getter_access_tracker["TextBox6"] = {}
		return self._TextBox6
	@TextBox6.setter
	def TextBox6(self, new_state):
		self._setter_access_tracker["TextBox6"] = {}
		global default_state
		self._TextBox6 = TextBox(new_state, default_state["TextBox6"])

	@property
	def p_Home_Button1_bpt(self):
		self._getter_access_tracker["p_Home_Button1_bpt"] = {}
		return self._p_Home_Button1_bpt
	@p_Home_Button1_bpt.setter
	def p_Home_Button1_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button1_bpt"] = {}
		global default_state
		self._p_Home_Button1_bpt = Button(new_state, default_state["p_Home_Button1_bpt"])

	@property
	def p_Home_Button2_bpt(self):
		self._getter_access_tracker["p_Home_Button2_bpt"] = {}
		return self._p_Home_Button2_bpt
	@p_Home_Button2_bpt.setter
	def p_Home_Button2_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button2_bpt"] = {}
		global default_state
		self._p_Home_Button2_bpt = Button(new_state, default_state["p_Home_Button2_bpt"])

	@property
	def TextBox11(self):
		self._getter_access_tracker["TextBox11"] = {}
		return self._TextBox11
	@TextBox11.setter
	def TextBox11(self, new_state):
		self._setter_access_tracker["TextBox11"] = {}
		global default_state
		self._TextBox11 = TextBox(new_state, default_state["TextBox11"])

	@property
	def p_Home_Button3_bpt(self):
		self._getter_access_tracker["p_Home_Button3_bpt"] = {}
		return self._p_Home_Button3_bpt
	@p_Home_Button3_bpt.setter
	def p_Home_Button3_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button3_bpt"] = {}
		global default_state
		self._p_Home_Button3_bpt = Button(new_state, default_state["p_Home_Button3_bpt"])

	@property
	def p_Home_Button4_bpt(self):
		self._getter_access_tracker["p_Home_Button4_bpt"] = {}
		return self._p_Home_Button4_bpt
	@p_Home_Button4_bpt.setter
	def p_Home_Button4_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button4_bpt"] = {}
		global default_state
		self._p_Home_Button4_bpt = Button(new_state, default_state["p_Home_Button4_bpt"])

	@property
	def TextBox9(self):
		self._getter_access_tracker["TextBox9"] = {}
		return self._TextBox9
	@TextBox9.setter
	def TextBox9(self, new_state):
		self._setter_access_tracker["TextBox9"] = {}
		global default_state
		self._TextBox9 = TextBox(new_state, default_state["TextBox9"])

	@property
	def TextBox10(self):
		self._getter_access_tracker["TextBox10"] = {}
		return self._TextBox10
	@TextBox10.setter
	def TextBox10(self, new_state):
		self._setter_access_tracker["TextBox10"] = {}
		global default_state
		self._TextBox10 = TextBox(new_state, default_state["TextBox10"])

	@property
	def p_Home_Image5_bpt(self):
		self._getter_access_tracker["p_Home_Image5_bpt"] = {}
		return self._p_Home_Image5_bpt
	@p_Home_Image5_bpt.setter
	def p_Home_Image5_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image5_bpt"] = {}
		global default_state
		self._p_Home_Image5_bpt = Image(new_state, default_state["p_Home_Image5_bpt"])

	@property
	def TextBox12(self):
		self._getter_access_tracker["TextBox12"] = {}
		return self._TextBox12
	@TextBox12.setter
	def TextBox12(self, new_state):
		self._setter_access_tracker["TextBox12"] = {}
		global default_state
		self._TextBox12 = TextBox(new_state, default_state["TextBox12"])

	@property
	def p_Home_Image6_bpt(self):
		self._getter_access_tracker["p_Home_Image6_bpt"] = {}
		return self._p_Home_Image6_bpt
	@p_Home_Image6_bpt.setter
	def p_Home_Image6_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image6_bpt"] = {}
		global default_state
		self._p_Home_Image6_bpt = Image(new_state, default_state["p_Home_Image6_bpt"])

	@property
	def p_Home_Image10_bpt(self):
		self._getter_access_tracker["p_Home_Image10_bpt"] = {}
		return self._p_Home_Image10_bpt
	@p_Home_Image10_bpt.setter
	def p_Home_Image10_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image10_bpt"] = {}
		global default_state
		self._p_Home_Image10_bpt = Image(new_state, default_state["p_Home_Image10_bpt"])

	@property
	def p_Home_Image198_bpt(self):
		self._getter_access_tracker["p_Home_Image198_bpt"] = {}
		return self._p_Home_Image198_bpt
	@p_Home_Image198_bpt.setter
	def p_Home_Image198_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image198_bpt"] = {}
		global default_state
		self._p_Home_Image198_bpt = Image(new_state, default_state["p_Home_Image198_bpt"])

	@property
	def p_Home_Image197_bpt(self):
		self._getter_access_tracker["p_Home_Image197_bpt"] = {}
		return self._p_Home_Image197_bpt
	@p_Home_Image197_bpt.setter
	def p_Home_Image197_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image197_bpt"] = {}
		global default_state
		self._p_Home_Image197_bpt = Image(new_state, default_state["p_Home_Image197_bpt"])

	@property
	def p_Home_TextBox11_bpt(self):
		self._getter_access_tracker["p_Home_TextBox11_bpt"] = {}
		return self._p_Home_TextBox11_bpt
	@p_Home_TextBox11_bpt.setter
	def p_Home_TextBox11_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox11_bpt"] = {}
		global default_state
		self._p_Home_TextBox11_bpt = TextBox(new_state, default_state["p_Home_TextBox11_bpt"])

	@property
	def p_Home_Image11_bpt(self):
		self._getter_access_tracker["p_Home_Image11_bpt"] = {}
		return self._p_Home_Image11_bpt
	@p_Home_Image11_bpt.setter
	def p_Home_Image11_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image11_bpt"] = {}
		global default_state
		self._p_Home_Image11_bpt = Image(new_state, default_state["p_Home_Image11_bpt"])

	@property
	def p_Home_TextBox13_bpt(self):
		self._getter_access_tracker["p_Home_TextBox13_bpt"] = {}
		return self._p_Home_TextBox13_bpt
	@p_Home_TextBox13_bpt.setter
	def p_Home_TextBox13_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox13_bpt"] = {}
		global default_state
		self._p_Home_TextBox13_bpt = TextBox(new_state, default_state["p_Home_TextBox13_bpt"])

	@property
	def p_Home_TextBox14_bpt(self):
		self._getter_access_tracker["p_Home_TextBox14_bpt"] = {}
		return self._p_Home_TextBox14_bpt
	@p_Home_TextBox14_bpt.setter
	def p_Home_TextBox14_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox14_bpt"] = {}
		global default_state
		self._p_Home_TextBox14_bpt = TextBox(new_state, default_state["p_Home_TextBox14_bpt"])

	@property
	def p_Home_TextBox12_bpt(self):
		self._getter_access_tracker["p_Home_TextBox12_bpt"] = {}
		return self._p_Home_TextBox12_bpt
	@p_Home_TextBox12_bpt.setter
	def p_Home_TextBox12_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox12_bpt"] = {}
		global default_state
		self._p_Home_TextBox12_bpt = TextBox(new_state, default_state["p_Home_TextBox12_bpt"])

	@property
	def p_Home_Image195_bpt(self):
		self._getter_access_tracker["p_Home_Image195_bpt"] = {}
		return self._p_Home_Image195_bpt
	@p_Home_Image195_bpt.setter
	def p_Home_Image195_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image195_bpt"] = {}
		global default_state
		self._p_Home_Image195_bpt = Image(new_state, default_state["p_Home_Image195_bpt"])

	@property
	def p_Home_TextBox383_bpt(self):
		self._getter_access_tracker["p_Home_TextBox383_bpt"] = {}
		return self._p_Home_TextBox383_bpt
	@p_Home_TextBox383_bpt.setter
	def p_Home_TextBox383_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox383_bpt"] = {}
		global default_state
		self._p_Home_TextBox383_bpt = TextBox(new_state, default_state["p_Home_TextBox383_bpt"])

	@property
	def p_Home_TextBox384_bpt(self):
		self._getter_access_tracker["p_Home_TextBox384_bpt"] = {}
		return self._p_Home_TextBox384_bpt
	@p_Home_TextBox384_bpt.setter
	def p_Home_TextBox384_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox384_bpt"] = {}
		global default_state
		self._p_Home_TextBox384_bpt = TextBox(new_state, default_state["p_Home_TextBox384_bpt"])

	@property
	def p_Home_TextBox382_bpt(self):
		self._getter_access_tracker["p_Home_TextBox382_bpt"] = {}
		return self._p_Home_TextBox382_bpt
	@p_Home_TextBox382_bpt.setter
	def p_Home_TextBox382_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox382_bpt"] = {}
		global default_state
		self._p_Home_TextBox382_bpt = TextBox(new_state, default_state["p_Home_TextBox382_bpt"])

	@property
	def p_Home_TextBox32_bpt(self):
		self._getter_access_tracker["p_Home_TextBox32_bpt"] = {}
		return self._p_Home_TextBox32_bpt
	@p_Home_TextBox32_bpt.setter
	def p_Home_TextBox32_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox32_bpt"] = {}
		global default_state
		self._p_Home_TextBox32_bpt = TextBox(new_state, default_state["p_Home_TextBox32_bpt"])

	@property
	def p_Home_TextBox30_bpt(self):
		self._getter_access_tracker["p_Home_TextBox30_bpt"] = {}
		return self._p_Home_TextBox30_bpt
	@p_Home_TextBox30_bpt.setter
	def p_Home_TextBox30_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox30_bpt"] = {}
		global default_state
		self._p_Home_TextBox30_bpt = TextBox(new_state, default_state["p_Home_TextBox30_bpt"])

	@property
	def p_Home_TextBox31_bpt(self):
		self._getter_access_tracker["p_Home_TextBox31_bpt"] = {}
		return self._p_Home_TextBox31_bpt
	@p_Home_TextBox31_bpt.setter
	def p_Home_TextBox31_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox31_bpt"] = {}
		global default_state
		self._p_Home_TextBox31_bpt = TextBox(new_state, default_state["p_Home_TextBox31_bpt"])

	@property
	def p_Home_Image17_bpt(self):
		self._getter_access_tracker["p_Home_Image17_bpt"] = {}
		return self._p_Home_Image17_bpt
	@p_Home_Image17_bpt.setter
	def p_Home_Image17_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image17_bpt"] = {}
		global default_state
		self._p_Home_Image17_bpt = Image(new_state, default_state["p_Home_Image17_bpt"])

	@property
	def p_Home_Image196_bpt(self):
		self._getter_access_tracker["p_Home_Image196_bpt"] = {}
		return self._p_Home_Image196_bpt
	@p_Home_Image196_bpt.setter
	def p_Home_Image196_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image196_bpt"] = {}
		global default_state
		self._p_Home_Image196_bpt = Image(new_state, default_state["p_Home_Image196_bpt"])

	@property
	def p_Home_TextBox386_bpt(self):
		self._getter_access_tracker["p_Home_TextBox386_bpt"] = {}
		return self._p_Home_TextBox386_bpt
	@p_Home_TextBox386_bpt.setter
	def p_Home_TextBox386_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox386_bpt"] = {}
		global default_state
		self._p_Home_TextBox386_bpt = TextBox(new_state, default_state["p_Home_TextBox386_bpt"])

	@property
	def p_Home_TextBox387_bpt(self):
		self._getter_access_tracker["p_Home_TextBox387_bpt"] = {}
		return self._p_Home_TextBox387_bpt
	@p_Home_TextBox387_bpt.setter
	def p_Home_TextBox387_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox387_bpt"] = {}
		global default_state
		self._p_Home_TextBox387_bpt = TextBox(new_state, default_state["p_Home_TextBox387_bpt"])

	@property
	def p_Home_TextBox385_bpt(self):
		self._getter_access_tracker["p_Home_TextBox385_bpt"] = {}
		return self._p_Home_TextBox385_bpt
	@p_Home_TextBox385_bpt.setter
	def p_Home_TextBox385_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox385_bpt"] = {}
		global default_state
		self._p_Home_TextBox385_bpt = TextBox(new_state, default_state["p_Home_TextBox385_bpt"])

	@property
	def p_Home_Button9_bpt(self):
		self._getter_access_tracker["p_Home_Button9_bpt"] = {}
		return self._p_Home_Button9_bpt
	@p_Home_Button9_bpt.setter
	def p_Home_Button9_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button9_bpt"] = {}
		global default_state
		self._p_Home_Button9_bpt = Button(new_state, default_state["p_Home_Button9_bpt"])

	@property
	def p_Home_Button10_bpt(self):
		self._getter_access_tracker["p_Home_Button10_bpt"] = {}
		return self._p_Home_Button10_bpt
	@p_Home_Button10_bpt.setter
	def p_Home_Button10_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button10_bpt"] = {}
		global default_state
		self._p_Home_Button10_bpt = Button(new_state, default_state["p_Home_Button10_bpt"])

	@property
	def p_Home_Image19_bpt(self):
		self._getter_access_tracker["p_Home_Image19_bpt"] = {}
		return self._p_Home_Image19_bpt
	@p_Home_Image19_bpt.setter
	def p_Home_Image19_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image19_bpt"] = {}
		global default_state
		self._p_Home_Image19_bpt = Image(new_state, default_state["p_Home_Image19_bpt"])

	@property
	def p_Home_TextBox36_bpt(self):
		self._getter_access_tracker["p_Home_TextBox36_bpt"] = {}
		return self._p_Home_TextBox36_bpt
	@p_Home_TextBox36_bpt.setter
	def p_Home_TextBox36_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox36_bpt"] = {}
		global default_state
		self._p_Home_TextBox36_bpt = TextBox(new_state, default_state["p_Home_TextBox36_bpt"])

	@property
	def p_Home_Image20_bpt(self):
		self._getter_access_tracker["p_Home_Image20_bpt"] = {}
		return self._p_Home_Image20_bpt
	@p_Home_Image20_bpt.setter
	def p_Home_Image20_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image20_bpt"] = {}
		global default_state
		self._p_Home_Image20_bpt = Image(new_state, default_state["p_Home_Image20_bpt"])

	@property
	def p_Home_TextBox38_bpt(self):
		self._getter_access_tracker["p_Home_TextBox38_bpt"] = {}
		return self._p_Home_TextBox38_bpt
	@p_Home_TextBox38_bpt.setter
	def p_Home_TextBox38_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox38_bpt"] = {}
		global default_state
		self._p_Home_TextBox38_bpt = TextBox(new_state, default_state["p_Home_TextBox38_bpt"])

	@property
	def p_Home_Image25_bpt(self):
		self._getter_access_tracker["p_Home_Image25_bpt"] = {}
		return self._p_Home_Image25_bpt
	@p_Home_Image25_bpt.setter
	def p_Home_Image25_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image25_bpt"] = {}
		global default_state
		self._p_Home_Image25_bpt = Image(new_state, default_state["p_Home_Image25_bpt"])

	@property
	def p_Home_TextBox43_bpt(self):
		self._getter_access_tracker["p_Home_TextBox43_bpt"] = {}
		return self._p_Home_TextBox43_bpt
	@p_Home_TextBox43_bpt.setter
	def p_Home_TextBox43_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox43_bpt"] = {}
		global default_state
		self._p_Home_TextBox43_bpt = TextBox(new_state, default_state["p_Home_TextBox43_bpt"])

	@property
	def p_Home_Image22_bpt(self):
		self._getter_access_tracker["p_Home_Image22_bpt"] = {}
		return self._p_Home_Image22_bpt
	@p_Home_Image22_bpt.setter
	def p_Home_Image22_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image22_bpt"] = {}
		global default_state
		self._p_Home_Image22_bpt = Image(new_state, default_state["p_Home_Image22_bpt"])

	@property
	def p_Home_TextBox40_bpt(self):
		self._getter_access_tracker["p_Home_TextBox40_bpt"] = {}
		return self._p_Home_TextBox40_bpt
	@p_Home_TextBox40_bpt.setter
	def p_Home_TextBox40_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox40_bpt"] = {}
		global default_state
		self._p_Home_TextBox40_bpt = TextBox(new_state, default_state["p_Home_TextBox40_bpt"])

	@property
	def p_Home_TextBox44_bpt(self):
		self._getter_access_tracker["p_Home_TextBox44_bpt"] = {}
		return self._p_Home_TextBox44_bpt
	@p_Home_TextBox44_bpt.setter
	def p_Home_TextBox44_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox44_bpt"] = {}
		global default_state
		self._p_Home_TextBox44_bpt = TextBox(new_state, default_state["p_Home_TextBox44_bpt"])

	@property
	def p_Home_TextBox45_bpt(self):
		self._getter_access_tracker["p_Home_TextBox45_bpt"] = {}
		return self._p_Home_TextBox45_bpt
	@p_Home_TextBox45_bpt.setter
	def p_Home_TextBox45_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox45_bpt"] = {}
		global default_state
		self._p_Home_TextBox45_bpt = TextBox(new_state, default_state["p_Home_TextBox45_bpt"])

	@property
	def p_Home_TextBox46_bpt(self):
		self._getter_access_tracker["p_Home_TextBox46_bpt"] = {}
		return self._p_Home_TextBox46_bpt
	@p_Home_TextBox46_bpt.setter
	def p_Home_TextBox46_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox46_bpt"] = {}
		global default_state
		self._p_Home_TextBox46_bpt = TextBox(new_state, default_state["p_Home_TextBox46_bpt"])

	@property
	def p_Home_Button12_bpt(self):
		self._getter_access_tracker["p_Home_Button12_bpt"] = {}
		return self._p_Home_Button12_bpt
	@p_Home_Button12_bpt.setter
	def p_Home_Button12_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button12_bpt"] = {}
		global default_state
		self._p_Home_Button12_bpt = Button(new_state, default_state["p_Home_Button12_bpt"])

	@property
	def p_Home_Button11_bpt(self):
		self._getter_access_tracker["p_Home_Button11_bpt"] = {}
		return self._p_Home_Button11_bpt
	@p_Home_Button11_bpt.setter
	def p_Home_Button11_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button11_bpt"] = {}
		global default_state
		self._p_Home_Button11_bpt = Button(new_state, default_state["p_Home_Button11_bpt"])

	@property
	def p_Home_TextBox47_bpt(self):
		self._getter_access_tracker["p_Home_TextBox47_bpt"] = {}
		return self._p_Home_TextBox47_bpt
	@p_Home_TextBox47_bpt.setter
	def p_Home_TextBox47_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox47_bpt"] = {}
		global default_state
		self._p_Home_TextBox47_bpt = TextBox(new_state, default_state["p_Home_TextBox47_bpt"])

	@property
	def p_Home_TextBox48_bpt(self):
		self._getter_access_tracker["p_Home_TextBox48_bpt"] = {}
		return self._p_Home_TextBox48_bpt
	@p_Home_TextBox48_bpt.setter
	def p_Home_TextBox48_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox48_bpt"] = {}
		global default_state
		self._p_Home_TextBox48_bpt = TextBox(new_state, default_state["p_Home_TextBox48_bpt"])

	@property
	def p_Home_Product_Name_1_bpt(self):
		self._getter_access_tracker["p_Home_Product_Name_1_bpt"] = {}
		return self._p_Home_Product_Name_1_bpt
	@p_Home_Product_Name_1_bpt.setter
	def p_Home_Product_Name_1_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Name_1_bpt"] = {}
		global default_state
		self._p_Home_Product_Name_1_bpt = TextBox(new_state, default_state["p_Home_Product_Name_1_bpt"])

	@property
	def p_Home_Product_About_1_bpt(self):
		self._getter_access_tracker["p_Home_Product_About_1_bpt"] = {}
		return self._p_Home_Product_About_1_bpt
	@p_Home_Product_About_1_bpt.setter
	def p_Home_Product_About_1_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_About_1_bpt"] = {}
		global default_state
		self._p_Home_Product_About_1_bpt = TextBox(new_state, default_state["p_Home_Product_About_1_bpt"])

	@property
	def p_Home_Product_Image_1_bpt(self):
		self._getter_access_tracker["p_Home_Product_Image_1_bpt"] = {}
		return self._p_Home_Product_Image_1_bpt
	@p_Home_Product_Image_1_bpt.setter
	def p_Home_Product_Image_1_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Image_1_bpt"] = {}
		global default_state
		self._p_Home_Product_Image_1_bpt = Image(new_state, default_state["p_Home_Product_Image_1_bpt"])

	@property
	def p_Home_Product_Price_1_bpt(self):
		self._getter_access_tracker["p_Home_Product_Price_1_bpt"] = {}
		return self._p_Home_Product_Price_1_bpt
	@p_Home_Product_Price_1_bpt.setter
	def p_Home_Product_Price_1_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Price_1_bpt"] = {}
		global default_state
		self._p_Home_Product_Price_1_bpt = TextBox(new_state, default_state["p_Home_Product_Price_1_bpt"])

	@property
	def p_Home_Product_Image_2_bpt(self):
		self._getter_access_tracker["p_Home_Product_Image_2_bpt"] = {}
		return self._p_Home_Product_Image_2_bpt
	@p_Home_Product_Image_2_bpt.setter
	def p_Home_Product_Image_2_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Image_2_bpt"] = {}
		global default_state
		self._p_Home_Product_Image_2_bpt = Image(new_state, default_state["p_Home_Product_Image_2_bpt"])

	@property
	def p_Home_Product_About_2_bpt(self):
		self._getter_access_tracker["p_Home_Product_About_2_bpt"] = {}
		return self._p_Home_Product_About_2_bpt
	@p_Home_Product_About_2_bpt.setter
	def p_Home_Product_About_2_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_About_2_bpt"] = {}
		global default_state
		self._p_Home_Product_About_2_bpt = TextBox(new_state, default_state["p_Home_Product_About_2_bpt"])

	@property
	def p_Home_Product_Name_2_bpt(self):
		self._getter_access_tracker["p_Home_Product_Name_2_bpt"] = {}
		return self._p_Home_Product_Name_2_bpt
	@p_Home_Product_Name_2_bpt.setter
	def p_Home_Product_Name_2_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Name_2_bpt"] = {}
		global default_state
		self._p_Home_Product_Name_2_bpt = TextBox(new_state, default_state["p_Home_Product_Name_2_bpt"])

	@property
	def p_Home_Product_Price_2_bpt(self):
		self._getter_access_tracker["p_Home_Product_Price_2_bpt"] = {}
		return self._p_Home_Product_Price_2_bpt
	@p_Home_Product_Price_2_bpt.setter
	def p_Home_Product_Price_2_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Price_2_bpt"] = {}
		global default_state
		self._p_Home_Product_Price_2_bpt = TextBox(new_state, default_state["p_Home_Product_Price_2_bpt"])

	@property
	def p_Home_Product_Name_4_bpt(self):
		self._getter_access_tracker["p_Home_Product_Name_4_bpt"] = {}
		return self._p_Home_Product_Name_4_bpt
	@p_Home_Product_Name_4_bpt.setter
	def p_Home_Product_Name_4_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Name_4_bpt"] = {}
		global default_state
		self._p_Home_Product_Name_4_bpt = TextBox(new_state, default_state["p_Home_Product_Name_4_bpt"])

	@property
	def p_Home_Product_About_4_bpt(self):
		self._getter_access_tracker["p_Home_Product_About_4_bpt"] = {}
		return self._p_Home_Product_About_4_bpt
	@p_Home_Product_About_4_bpt.setter
	def p_Home_Product_About_4_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_About_4_bpt"] = {}
		global default_state
		self._p_Home_Product_About_4_bpt = TextBox(new_state, default_state["p_Home_Product_About_4_bpt"])

	@property
	def p_Home_Product_Image_4_bpt(self):
		self._getter_access_tracker["p_Home_Product_Image_4_bpt"] = {}
		return self._p_Home_Product_Image_4_bpt
	@p_Home_Product_Image_4_bpt.setter
	def p_Home_Product_Image_4_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Image_4_bpt"] = {}
		global default_state
		self._p_Home_Product_Image_4_bpt = Image(new_state, default_state["p_Home_Product_Image_4_bpt"])

	@property
	def p_Home_Product_Price_4_bpt(self):
		self._getter_access_tracker["p_Home_Product_Price_4_bpt"] = {}
		return self._p_Home_Product_Price_4_bpt
	@p_Home_Product_Price_4_bpt.setter
	def p_Home_Product_Price_4_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Price_4_bpt"] = {}
		global default_state
		self._p_Home_Product_Price_4_bpt = TextBox(new_state, default_state["p_Home_Product_Price_4_bpt"])

	@property
	def p_Home_Product_Image_3_bpt(self):
		self._getter_access_tracker["p_Home_Product_Image_3_bpt"] = {}
		return self._p_Home_Product_Image_3_bpt
	@p_Home_Product_Image_3_bpt.setter
	def p_Home_Product_Image_3_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Image_3_bpt"] = {}
		global default_state
		self._p_Home_Product_Image_3_bpt = Image(new_state, default_state["p_Home_Product_Image_3_bpt"])

	@property
	def p_Home_Product_About_3_bpt(self):
		self._getter_access_tracker["p_Home_Product_About_3_bpt"] = {}
		return self._p_Home_Product_About_3_bpt
	@p_Home_Product_About_3_bpt.setter
	def p_Home_Product_About_3_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_About_3_bpt"] = {}
		global default_state
		self._p_Home_Product_About_3_bpt = TextBox(new_state, default_state["p_Home_Product_About_3_bpt"])

	@property
	def p_Home_Product_Name_3_bpt(self):
		self._getter_access_tracker["p_Home_Product_Name_3_bpt"] = {}
		return self._p_Home_Product_Name_3_bpt
	@p_Home_Product_Name_3_bpt.setter
	def p_Home_Product_Name_3_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Name_3_bpt"] = {}
		global default_state
		self._p_Home_Product_Name_3_bpt = TextBox(new_state, default_state["p_Home_Product_Name_3_bpt"])

	@property
	def p_Home_Product_Price_3_bpt(self):
		self._getter_access_tracker["p_Home_Product_Price_3_bpt"] = {}
		return self._p_Home_Product_Price_3_bpt
	@p_Home_Product_Price_3_bpt.setter
	def p_Home_Product_Price_3_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Price_3_bpt"] = {}
		global default_state
		self._p_Home_Product_Price_3_bpt = TextBox(new_state, default_state["p_Home_Product_Price_3_bpt"])

	@property
	def p_Home_Button14_bpt(self):
		self._getter_access_tracker["p_Home_Button14_bpt"] = {}
		return self._p_Home_Button14_bpt
	@p_Home_Button14_bpt.setter
	def p_Home_Button14_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button14_bpt"] = {}
		global default_state
		self._p_Home_Button14_bpt = Button(new_state, default_state["p_Home_Button14_bpt"])

	@property
	def p_Home_Button13_bpt(self):
		self._getter_access_tracker["p_Home_Button13_bpt"] = {}
		return self._p_Home_Button13_bpt
	@p_Home_Button13_bpt.setter
	def p_Home_Button13_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button13_bpt"] = {}
		global default_state
		self._p_Home_Button13_bpt = Button(new_state, default_state["p_Home_Button13_bpt"])

	@property
	def p_Home_Product_Name_7_bpt(self):
		self._getter_access_tracker["p_Home_Product_Name_7_bpt"] = {}
		return self._p_Home_Product_Name_7_bpt
	@p_Home_Product_Name_7_bpt.setter
	def p_Home_Product_Name_7_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Name_7_bpt"] = {}
		global default_state
		self._p_Home_Product_Name_7_bpt = TextBox(new_state, default_state["p_Home_Product_Name_7_bpt"])

	@property
	def p_Home_Product_About_7_bpt(self):
		self._getter_access_tracker["p_Home_Product_About_7_bpt"] = {}
		return self._p_Home_Product_About_7_bpt
	@p_Home_Product_About_7_bpt.setter
	def p_Home_Product_About_7_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_About_7_bpt"] = {}
		global default_state
		self._p_Home_Product_About_7_bpt = TextBox(new_state, default_state["p_Home_Product_About_7_bpt"])

	@property
	def p_Home_Product_Image_7_bpt(self):
		self._getter_access_tracker["p_Home_Product_Image_7_bpt"] = {}
		return self._p_Home_Product_Image_7_bpt
	@p_Home_Product_Image_7_bpt.setter
	def p_Home_Product_Image_7_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Image_7_bpt"] = {}
		global default_state
		self._p_Home_Product_Image_7_bpt = Image(new_state, default_state["p_Home_Product_Image_7_bpt"])

	@property
	def p_Home_Product_Price_7_bpt(self):
		self._getter_access_tracker["p_Home_Product_Price_7_bpt"] = {}
		return self._p_Home_Product_Price_7_bpt
	@p_Home_Product_Price_7_bpt.setter
	def p_Home_Product_Price_7_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Price_7_bpt"] = {}
		global default_state
		self._p_Home_Product_Price_7_bpt = TextBox(new_state, default_state["p_Home_Product_Price_7_bpt"])

	@property
	def p_Home_Product_Image_8_bpt(self):
		self._getter_access_tracker["p_Home_Product_Image_8_bpt"] = {}
		return self._p_Home_Product_Image_8_bpt
	@p_Home_Product_Image_8_bpt.setter
	def p_Home_Product_Image_8_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Image_8_bpt"] = {}
		global default_state
		self._p_Home_Product_Image_8_bpt = Image(new_state, default_state["p_Home_Product_Image_8_bpt"])

	@property
	def p_Home_Product_About_8_bpt(self):
		self._getter_access_tracker["p_Home_Product_About_8_bpt"] = {}
		return self._p_Home_Product_About_8_bpt
	@p_Home_Product_About_8_bpt.setter
	def p_Home_Product_About_8_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_About_8_bpt"] = {}
		global default_state
		self._p_Home_Product_About_8_bpt = TextBox(new_state, default_state["p_Home_Product_About_8_bpt"])

	@property
	def p_Home_Product_Name_8_bpt(self):
		self._getter_access_tracker["p_Home_Product_Name_8_bpt"] = {}
		return self._p_Home_Product_Name_8_bpt
	@p_Home_Product_Name_8_bpt.setter
	def p_Home_Product_Name_8_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Name_8_bpt"] = {}
		global default_state
		self._p_Home_Product_Name_8_bpt = TextBox(new_state, default_state["p_Home_Product_Name_8_bpt"])

	@property
	def p_Home_Product_Price_8_bpt(self):
		self._getter_access_tracker["p_Home_Product_Price_8_bpt"] = {}
		return self._p_Home_Product_Price_8_bpt
	@p_Home_Product_Price_8_bpt.setter
	def p_Home_Product_Price_8_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Price_8_bpt"] = {}
		global default_state
		self._p_Home_Product_Price_8_bpt = TextBox(new_state, default_state["p_Home_Product_Price_8_bpt"])

	@property
	def p_Home_Product_Name_6_bpt(self):
		self._getter_access_tracker["p_Home_Product_Name_6_bpt"] = {}
		return self._p_Home_Product_Name_6_bpt
	@p_Home_Product_Name_6_bpt.setter
	def p_Home_Product_Name_6_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Name_6_bpt"] = {}
		global default_state
		self._p_Home_Product_Name_6_bpt = TextBox(new_state, default_state["p_Home_Product_Name_6_bpt"])

	@property
	def TextBox67(self):
		self._getter_access_tracker["TextBox67"] = {}
		return self._TextBox67
	@TextBox67.setter
	def TextBox67(self, new_state):
		self._setter_access_tracker["TextBox67"] = {}
		global default_state
		self._TextBox67 = TextBox(new_state, default_state["TextBox67"])

	@property
	def p_Home_Product_Image_6_bpt(self):
		self._getter_access_tracker["p_Home_Product_Image_6_bpt"] = {}
		return self._p_Home_Product_Image_6_bpt
	@p_Home_Product_Image_6_bpt.setter
	def p_Home_Product_Image_6_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Image_6_bpt"] = {}
		global default_state
		self._p_Home_Product_Image_6_bpt = Image(new_state, default_state["p_Home_Product_Image_6_bpt"])

	@property
	def p_Home_Product_Price_6_bpt(self):
		self._getter_access_tracker["p_Home_Product_Price_6_bpt"] = {}
		return self._p_Home_Product_Price_6_bpt
	@p_Home_Product_Price_6_bpt.setter
	def p_Home_Product_Price_6_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Price_6_bpt"] = {}
		global default_state
		self._p_Home_Product_Price_6_bpt = TextBox(new_state, default_state["p_Home_Product_Price_6_bpt"])

	@property
	def p_Home_Product_Image_5_bpt(self):
		self._getter_access_tracker["p_Home_Product_Image_5_bpt"] = {}
		return self._p_Home_Product_Image_5_bpt
	@p_Home_Product_Image_5_bpt.setter
	def p_Home_Product_Image_5_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Image_5_bpt"] = {}
		global default_state
		self._p_Home_Product_Image_5_bpt = Image(new_state, default_state["p_Home_Product_Image_5_bpt"])

	@property
	def p_Home_Product_About_5_bpt(self):
		self._getter_access_tracker["p_Home_Product_About_5_bpt"] = {}
		return self._p_Home_Product_About_5_bpt
	@p_Home_Product_About_5_bpt.setter
	def p_Home_Product_About_5_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_About_5_bpt"] = {}
		global default_state
		self._p_Home_Product_About_5_bpt = TextBox(new_state, default_state["p_Home_Product_About_5_bpt"])

	@property
	def p_Home_Product_Name_5_bpt(self):
		self._getter_access_tracker["p_Home_Product_Name_5_bpt"] = {}
		return self._p_Home_Product_Name_5_bpt
	@p_Home_Product_Name_5_bpt.setter
	def p_Home_Product_Name_5_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Name_5_bpt"] = {}
		global default_state
		self._p_Home_Product_Name_5_bpt = TextBox(new_state, default_state["p_Home_Product_Name_5_bpt"])

	@property
	def p_Home_Product_Price_5_bpt(self):
		self._getter_access_tracker["p_Home_Product_Price_5_bpt"] = {}
		return self._p_Home_Product_Price_5_bpt
	@p_Home_Product_Price_5_bpt.setter
	def p_Home_Product_Price_5_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Product_Price_5_bpt"] = {}
		global default_state
		self._p_Home_Product_Price_5_bpt = TextBox(new_state, default_state["p_Home_Product_Price_5_bpt"])

	@property
	def p_Home_TextBox73_bpt(self):
		self._getter_access_tracker["p_Home_TextBox73_bpt"] = {}
		return self._p_Home_TextBox73_bpt
	@p_Home_TextBox73_bpt.setter
	def p_Home_TextBox73_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox73_bpt"] = {}
		global default_state
		self._p_Home_TextBox73_bpt = TextBox(new_state, default_state["p_Home_TextBox73_bpt"])

	@property
	def p_Home_TextBox74_bpt(self):
		self._getter_access_tracker["p_Home_TextBox74_bpt"] = {}
		return self._p_Home_TextBox74_bpt
	@p_Home_TextBox74_bpt.setter
	def p_Home_TextBox74_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox74_bpt"] = {}
		global default_state
		self._p_Home_TextBox74_bpt = TextBox(new_state, default_state["p_Home_TextBox74_bpt"])

	@property
	def p_Home_Button16_bpt(self):
		self._getter_access_tracker["p_Home_Button16_bpt"] = {}
		return self._p_Home_Button16_bpt
	@p_Home_Button16_bpt.setter
	def p_Home_Button16_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button16_bpt"] = {}
		global default_state
		self._p_Home_Button16_bpt = Button(new_state, default_state["p_Home_Button16_bpt"])

	@property
	def p_Home_Button15_bpt(self):
		self._getter_access_tracker["p_Home_Button15_bpt"] = {}
		return self._p_Home_Button15_bpt
	@p_Home_Button15_bpt.setter
	def p_Home_Button15_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button15_bpt"] = {}
		global default_state
		self._p_Home_Button15_bpt = Button(new_state, default_state["p_Home_Button15_bpt"])

	@property
	def p_Home_Image34_bpt(self):
		self._getter_access_tracker["p_Home_Image34_bpt"] = {}
		return self._p_Home_Image34_bpt
	@p_Home_Image34_bpt.setter
	def p_Home_Image34_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image34_bpt"] = {}
		global default_state
		self._p_Home_Image34_bpt = Image(new_state, default_state["p_Home_Image34_bpt"])

	@property
	def p_Home_TextBox75_bpt(self):
		self._getter_access_tracker["p_Home_TextBox75_bpt"] = {}
		return self._p_Home_TextBox75_bpt
	@p_Home_TextBox75_bpt.setter
	def p_Home_TextBox75_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox75_bpt"] = {}
		global default_state
		self._p_Home_TextBox75_bpt = TextBox(new_state, default_state["p_Home_TextBox75_bpt"])

	@property
	def p_Home_TextBox76_bpt(self):
		self._getter_access_tracker["p_Home_TextBox76_bpt"] = {}
		return self._p_Home_TextBox76_bpt
	@p_Home_TextBox76_bpt.setter
	def p_Home_TextBox76_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox76_bpt"] = {}
		global default_state
		self._p_Home_TextBox76_bpt = TextBox(new_state, default_state["p_Home_TextBox76_bpt"])

	@property
	def p_Home_TextBox142_bpt(self):
		self._getter_access_tracker["p_Home_TextBox142_bpt"] = {}
		return self._p_Home_TextBox142_bpt
	@p_Home_TextBox142_bpt.setter
	def p_Home_TextBox142_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox142_bpt"] = {}
		global default_state
		self._p_Home_TextBox142_bpt = TextBox(new_state, default_state["p_Home_TextBox142_bpt"])

	@property
	def p_Home_Image74_bpt(self):
		self._getter_access_tracker["p_Home_Image74_bpt"] = {}
		return self._p_Home_Image74_bpt
	@p_Home_Image74_bpt.setter
	def p_Home_Image74_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image74_bpt"] = {}
		global default_state
		self._p_Home_Image74_bpt = Image(new_state, default_state["p_Home_Image74_bpt"])

	@property
	def p_Home_TextBox78_bpt(self):
		self._getter_access_tracker["p_Home_TextBox78_bpt"] = {}
		return self._p_Home_TextBox78_bpt
	@p_Home_TextBox78_bpt.setter
	def p_Home_TextBox78_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox78_bpt"] = {}
		global default_state
		self._p_Home_TextBox78_bpt = TextBox(new_state, default_state["p_Home_TextBox78_bpt"])

	@property
	def p_Home_TextBox79_bpt(self):
		self._getter_access_tracker["p_Home_TextBox79_bpt"] = {}
		return self._p_Home_TextBox79_bpt
	@p_Home_TextBox79_bpt.setter
	def p_Home_TextBox79_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox79_bpt"] = {}
		global default_state
		self._p_Home_TextBox79_bpt = TextBox(new_state, default_state["p_Home_TextBox79_bpt"])

	@property
	def p_Home_Image44_bpt(self):
		self._getter_access_tracker["p_Home_Image44_bpt"] = {}
		return self._p_Home_Image44_bpt
	@p_Home_Image44_bpt.setter
	def p_Home_Image44_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image44_bpt"] = {}
		global default_state
		self._p_Home_Image44_bpt = Image(new_state, default_state["p_Home_Image44_bpt"])

	@property
	def p_Home_Image76_bpt(self):
		self._getter_access_tracker["p_Home_Image76_bpt"] = {}
		return self._p_Home_Image76_bpt
	@p_Home_Image76_bpt.setter
	def p_Home_Image76_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image76_bpt"] = {}
		global default_state
		self._p_Home_Image76_bpt = Image(new_state, default_state["p_Home_Image76_bpt"])

	@property
	def p_Home_Image77_bpt(self):
		self._getter_access_tracker["p_Home_Image77_bpt"] = {}
		return self._p_Home_Image77_bpt
	@p_Home_Image77_bpt.setter
	def p_Home_Image77_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image77_bpt"] = {}
		global default_state
		self._p_Home_Image77_bpt = Image(new_state, default_state["p_Home_Image77_bpt"])

	@property
	def p_Home_Image78_bpt(self):
		self._getter_access_tracker["p_Home_Image78_bpt"] = {}
		return self._p_Home_Image78_bpt
	@p_Home_Image78_bpt.setter
	def p_Home_Image78_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image78_bpt"] = {}
		global default_state
		self._p_Home_Image78_bpt = Image(new_state, default_state["p_Home_Image78_bpt"])

	@property
	def p_Home_Image79_bpt(self):
		self._getter_access_tracker["p_Home_Image79_bpt"] = {}
		return self._p_Home_Image79_bpt
	@p_Home_Image79_bpt.setter
	def p_Home_Image79_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image79_bpt"] = {}
		global default_state
		self._p_Home_Image79_bpt = Image(new_state, default_state["p_Home_Image79_bpt"])

	@property
	def p_Home_Image40_bpt(self):
		self._getter_access_tracker["p_Home_Image40_bpt"] = {}
		return self._p_Home_Image40_bpt
	@p_Home_Image40_bpt.setter
	def p_Home_Image40_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image40_bpt"] = {}
		global default_state
		self._p_Home_Image40_bpt = Image(new_state, default_state["p_Home_Image40_bpt"])

	@property
	def p_Home_TextBox81_bpt(self):
		self._getter_access_tracker["p_Home_TextBox81_bpt"] = {}
		return self._p_Home_TextBox81_bpt
	@p_Home_TextBox81_bpt.setter
	def p_Home_TextBox81_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox81_bpt"] = {}
		global default_state
		self._p_Home_TextBox81_bpt = TextBox(new_state, default_state["p_Home_TextBox81_bpt"])

	@property
	def p_Home_TextBox80_bpt(self):
		self._getter_access_tracker["p_Home_TextBox80_bpt"] = {}
		return self._p_Home_TextBox80_bpt
	@p_Home_TextBox80_bpt.setter
	def p_Home_TextBox80_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox80_bpt"] = {}
		global default_state
		self._p_Home_TextBox80_bpt = TextBox(new_state, default_state["p_Home_TextBox80_bpt"])

	@property
	def p_Home_Image75_bpt(self):
		self._getter_access_tracker["p_Home_Image75_bpt"] = {}
		return self._p_Home_Image75_bpt
	@p_Home_Image75_bpt.setter
	def p_Home_Image75_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image75_bpt"] = {}
		global default_state
		self._p_Home_Image75_bpt = Image(new_state, default_state["p_Home_Image75_bpt"])

	@property
	def p_Home_Button17_bpt(self):
		self._getter_access_tracker["p_Home_Button17_bpt"] = {}
		return self._p_Home_Button17_bpt
	@p_Home_Button17_bpt.setter
	def p_Home_Button17_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button17_bpt"] = {}
		global default_state
		self._p_Home_Button17_bpt = Button(new_state, default_state["p_Home_Button17_bpt"])

	@property
	def p_Home_Button18_bpt(self):
		self._getter_access_tracker["p_Home_Button18_bpt"] = {}
		return self._p_Home_Button18_bpt
	@p_Home_Button18_bpt.setter
	def p_Home_Button18_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button18_bpt"] = {}
		global default_state
		self._p_Home_Button18_bpt = Button(new_state, default_state["p_Home_Button18_bpt"])

	@property
	def p_Home_TextBox82_bpt(self):
		self._getter_access_tracker["p_Home_TextBox82_bpt"] = {}
		return self._p_Home_TextBox82_bpt
	@p_Home_TextBox82_bpt.setter
	def p_Home_TextBox82_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox82_bpt"] = {}
		global default_state
		self._p_Home_TextBox82_bpt = TextBox(new_state, default_state["p_Home_TextBox82_bpt"])

	@property
	def p_Home_TextBox83_bpt(self):
		self._getter_access_tracker["p_Home_TextBox83_bpt"] = {}
		return self._p_Home_TextBox83_bpt
	@p_Home_TextBox83_bpt.setter
	def p_Home_TextBox83_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox83_bpt"] = {}
		global default_state
		self._p_Home_TextBox83_bpt = TextBox(new_state, default_state["p_Home_TextBox83_bpt"])

	@property
	def p_Home_Image45_bpt(self):
		self._getter_access_tracker["p_Home_Image45_bpt"] = {}
		return self._p_Home_Image45_bpt
	@p_Home_Image45_bpt.setter
	def p_Home_Image45_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image45_bpt"] = {}
		global default_state
		self._p_Home_Image45_bpt = Image(new_state, default_state["p_Home_Image45_bpt"])

	@property
	def p_Home_TextBox85_bpt(self):
		self._getter_access_tracker["p_Home_TextBox85_bpt"] = {}
		return self._p_Home_TextBox85_bpt
	@p_Home_TextBox85_bpt.setter
	def p_Home_TextBox85_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox85_bpt"] = {}
		global default_state
		self._p_Home_TextBox85_bpt = TextBox(new_state, default_state["p_Home_TextBox85_bpt"])

	@property
	def p_Home_TextBox86_bpt(self):
		self._getter_access_tracker["p_Home_TextBox86_bpt"] = {}
		return self._p_Home_TextBox86_bpt
	@p_Home_TextBox86_bpt.setter
	def p_Home_TextBox86_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox86_bpt"] = {}
		global default_state
		self._p_Home_TextBox86_bpt = TextBox(new_state, default_state["p_Home_TextBox86_bpt"])

	@property
	def p_Home_TextBox84_bpt(self):
		self._getter_access_tracker["p_Home_TextBox84_bpt"] = {}
		return self._p_Home_TextBox84_bpt
	@p_Home_TextBox84_bpt.setter
	def p_Home_TextBox84_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox84_bpt"] = {}
		global default_state
		self._p_Home_TextBox84_bpt = TextBox(new_state, default_state["p_Home_TextBox84_bpt"])

	@property
	def p_Home_Image49_bpt(self):
		self._getter_access_tracker["p_Home_Image49_bpt"] = {}
		return self._p_Home_Image49_bpt
	@p_Home_Image49_bpt.setter
	def p_Home_Image49_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image49_bpt"] = {}
		global default_state
		self._p_Home_Image49_bpt = Image(new_state, default_state["p_Home_Image49_bpt"])

	@property
	def p_Home_TextBox97_bpt(self):
		self._getter_access_tracker["p_Home_TextBox97_bpt"] = {}
		return self._p_Home_TextBox97_bpt
	@p_Home_TextBox97_bpt.setter
	def p_Home_TextBox97_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox97_bpt"] = {}
		global default_state
		self._p_Home_TextBox97_bpt = TextBox(new_state, default_state["p_Home_TextBox97_bpt"])

	@property
	def p_Home_TextBox96_bpt(self):
		self._getter_access_tracker["p_Home_TextBox96_bpt"] = {}
		return self._p_Home_TextBox96_bpt
	@p_Home_TextBox96_bpt.setter
	def p_Home_TextBox96_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox96_bpt"] = {}
		global default_state
		self._p_Home_TextBox96_bpt = TextBox(new_state, default_state["p_Home_TextBox96_bpt"])

	@property
	def p_Home_TextBox100_bpt(self):
		self._getter_access_tracker["p_Home_TextBox100_bpt"] = {}
		return self._p_Home_TextBox100_bpt
	@p_Home_TextBox100_bpt.setter
	def p_Home_TextBox100_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox100_bpt"] = {}
		global default_state
		self._p_Home_TextBox100_bpt = TextBox(new_state, default_state["p_Home_TextBox100_bpt"])

	@property
	def p_Home_TextBox99(self):
		self._getter_access_tracker["p_Home_TextBox99"] = {}
		return self._p_Home_TextBox99
	@p_Home_TextBox99.setter
	def p_Home_TextBox99(self, new_state):
		self._setter_access_tracker["p_Home_TextBox99"] = {}
		global default_state
		self._p_Home_TextBox99 = TextBox(new_state, default_state["p_Home_TextBox99"])

	@property
	def p_Home_Image51_bpt(self):
		self._getter_access_tracker["p_Home_Image51_bpt"] = {}
		return self._p_Home_Image51_bpt
	@p_Home_Image51_bpt.setter
	def p_Home_Image51_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image51_bpt"] = {}
		global default_state
		self._p_Home_Image51_bpt = Image(new_state, default_state["p_Home_Image51_bpt"])

	@property
	def p_Home_Image52_bpt(self):
		self._getter_access_tracker["p_Home_Image52_bpt"] = {}
		return self._p_Home_Image52_bpt
	@p_Home_Image52_bpt.setter
	def p_Home_Image52_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image52_bpt"] = {}
		global default_state
		self._p_Home_Image52_bpt = Image(new_state, default_state["p_Home_Image52_bpt"])

	@property
	def p_Home_TextBox102_bpt(self):
		self._getter_access_tracker["p_Home_TextBox102_bpt"] = {}
		return self._p_Home_TextBox102_bpt
	@p_Home_TextBox102_bpt.setter
	def p_Home_TextBox102_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox102_bpt"] = {}
		global default_state
		self._p_Home_TextBox102_bpt = TextBox(new_state, default_state["p_Home_TextBox102_bpt"])

	@property
	def p_Home_TextBox101_bpt(self):
		self._getter_access_tracker["p_Home_TextBox101_bpt"] = {}
		return self._p_Home_TextBox101_bpt
	@p_Home_TextBox101_bpt.setter
	def p_Home_TextBox101_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox101_bpt"] = {}
		global default_state
		self._p_Home_TextBox101_bpt = TextBox(new_state, default_state["p_Home_TextBox101_bpt"])

	@property
	def p_Home_TextBox104(self):
		self._getter_access_tracker["p_Home_TextBox104"] = {}
		return self._p_Home_TextBox104
	@p_Home_TextBox104.setter
	def p_Home_TextBox104(self, new_state):
		self._setter_access_tracker["p_Home_TextBox104"] = {}
		global default_state
		self._p_Home_TextBox104 = TextBox(new_state, default_state["p_Home_TextBox104"])

	@property
	def p_Home_TextBox103_bpt(self):
		self._getter_access_tracker["p_Home_TextBox103_bpt"] = {}
		return self._p_Home_TextBox103_bpt
	@p_Home_TextBox103_bpt.setter
	def p_Home_TextBox103_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox103_bpt"] = {}
		global default_state
		self._p_Home_TextBox103_bpt = TextBox(new_state, default_state["p_Home_TextBox103_bpt"])

	@property
	def p_Home_Image53_bpt(self):
		self._getter_access_tracker["p_Home_Image53_bpt"] = {}
		return self._p_Home_Image53_bpt
	@p_Home_Image53_bpt.setter
	def p_Home_Image53_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image53_bpt"] = {}
		global default_state
		self._p_Home_Image53_bpt = Image(new_state, default_state["p_Home_Image53_bpt"])

	@property
	def p_Home_Button21_bpt(self):
		self._getter_access_tracker["p_Home_Button21_bpt"] = {}
		return self._p_Home_Button21_bpt
	@p_Home_Button21_bpt.setter
	def p_Home_Button21_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Button21_bpt"] = {}
		global default_state
		self._p_Home_Button21_bpt = Button(new_state, default_state["p_Home_Button21_bpt"])

	@property
	def p_Home_TextBox113_bpt(self):
		self._getter_access_tracker["p_Home_TextBox113_bpt"] = {}
		return self._p_Home_TextBox113_bpt
	@p_Home_TextBox113_bpt.setter
	def p_Home_TextBox113_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox113_bpt"] = {}
		global default_state
		self._p_Home_TextBox113_bpt = TextBox(new_state, default_state["p_Home_TextBox113_bpt"])

	@property
	def p_Home_Input1_bpt(self):
		self._getter_access_tracker["p_Home_Input1_bpt"] = {}
		return self._p_Home_Input1_bpt
	@p_Home_Input1_bpt.setter
	def p_Home_Input1_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Input1_bpt"] = {}
		global default_state
		self._p_Home_Input1_bpt = Input(new_state, default_state["p_Home_Input1_bpt"])

	@property
	def p_Home_Input2_bpt(self):
		self._getter_access_tracker["p_Home_Input2_bpt"] = {}
		return self._p_Home_Input2_bpt
	@p_Home_Input2_bpt.setter
	def p_Home_Input2_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Input2_bpt"] = {}
		global default_state
		self._p_Home_Input2_bpt = Input(new_state, default_state["p_Home_Input2_bpt"])

	@property
	def p_Home_TextBox114_bpt(self):
		self._getter_access_tracker["p_Home_TextBox114_bpt"] = {}
		return self._p_Home_TextBox114_bpt
	@p_Home_TextBox114_bpt.setter
	def p_Home_TextBox114_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox114_bpt"] = {}
		global default_state
		self._p_Home_TextBox114_bpt = TextBox(new_state, default_state["p_Home_TextBox114_bpt"])

	@property
	def p_Home_Input4_bpt(self):
		self._getter_access_tracker["p_Home_Input4_bpt"] = {}
		return self._p_Home_Input4_bpt
	@p_Home_Input4_bpt.setter
	def p_Home_Input4_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Input4_bpt"] = {}
		global default_state
		self._p_Home_Input4_bpt = Input(new_state, default_state["p_Home_Input4_bpt"])

	@property
	def p_Home_TextBox116_bpt(self):
		self._getter_access_tracker["p_Home_TextBox116_bpt"] = {}
		return self._p_Home_TextBox116_bpt
	@p_Home_TextBox116_bpt.setter
	def p_Home_TextBox116_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox116_bpt"] = {}
		global default_state
		self._p_Home_TextBox116_bpt = TextBox(new_state, default_state["p_Home_TextBox116_bpt"])

	@property
	def p_Home_Input3_bpt(self):
		self._getter_access_tracker["p_Home_Input3_bpt"] = {}
		return self._p_Home_Input3_bpt
	@p_Home_Input3_bpt.setter
	def p_Home_Input3_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Input3_bpt"] = {}
		global default_state
		self._p_Home_Input3_bpt = Input(new_state, default_state["p_Home_Input3_bpt"])

	@property
	def p_Home_TextBox115_bpt(self):
		self._getter_access_tracker["p_Home_TextBox115_bpt"] = {}
		return self._p_Home_TextBox115_bpt
	@p_Home_TextBox115_bpt.setter
	def p_Home_TextBox115_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox115_bpt"] = {}
		global default_state
		self._p_Home_TextBox115_bpt = TextBox(new_state, default_state["p_Home_TextBox115_bpt"])

	@property
	def p_Home_TextBox118_bpt(self):
		self._getter_access_tracker["p_Home_TextBox118_bpt"] = {}
		return self._p_Home_TextBox118_bpt
	@p_Home_TextBox118_bpt.setter
	def p_Home_TextBox118_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox118_bpt"] = {}
		global default_state
		self._p_Home_TextBox118_bpt = TextBox(new_state, default_state["p_Home_TextBox118_bpt"])

	@property
	def p_Home_Input6_bpt(self):
		self._getter_access_tracker["p_Home_Input6_bpt"] = {}
		return self._p_Home_Input6_bpt
	@p_Home_Input6_bpt.setter
	def p_Home_Input6_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Input6_bpt"] = {}
		global default_state
		self._p_Home_Input6_bpt = Input(new_state, default_state["p_Home_Input6_bpt"])

	@property
	def p_Home_TextBox117_bpt(self):
		self._getter_access_tracker["p_Home_TextBox117_bpt"] = {}
		return self._p_Home_TextBox117_bpt
	@p_Home_TextBox117_bpt.setter
	def p_Home_TextBox117_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox117_bpt"] = {}
		global default_state
		self._p_Home_TextBox117_bpt = TextBox(new_state, default_state["p_Home_TextBox117_bpt"])

	@property
	def p_Home_Input5_bpt(self):
		self._getter_access_tracker["p_Home_Input5_bpt"] = {}
		return self._p_Home_Input5_bpt
	@p_Home_Input5_bpt.setter
	def p_Home_Input5_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Input5_bpt"] = {}
		global default_state
		self._p_Home_Input5_bpt = Input(new_state, default_state["p_Home_Input5_bpt"])

	@property
	def p_Home_TextBox120_bpt(self):
		self._getter_access_tracker["p_Home_TextBox120_bpt"] = {}
		return self._p_Home_TextBox120_bpt
	@p_Home_TextBox120_bpt.setter
	def p_Home_TextBox120_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox120_bpt"] = {}
		global default_state
		self._p_Home_TextBox120_bpt = TextBox(new_state, default_state["p_Home_TextBox120_bpt"])

	@property
	def p_Home_Input9_bpt(self):
		self._getter_access_tracker["p_Home_Input9_bpt"] = {}
		return self._p_Home_Input9_bpt
	@p_Home_Input9_bpt.setter
	def p_Home_Input9_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Input9_bpt"] = {}
		global default_state
		self._p_Home_Input9_bpt = Input(new_state, default_state["p_Home_Input9_bpt"])

	@property
	def p_Home_TextBox105_bpt(self):
		self._getter_access_tracker["p_Home_TextBox105_bpt"] = {}
		return self._p_Home_TextBox105_bpt
	@p_Home_TextBox105_bpt.setter
	def p_Home_TextBox105_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox105_bpt"] = {}
		global default_state
		self._p_Home_TextBox105_bpt = TextBox(new_state, default_state["p_Home_TextBox105_bpt"])

	@property
	def p_Home_TextBox106_bpt(self):
		self._getter_access_tracker["p_Home_TextBox106_bpt"] = {}
		return self._p_Home_TextBox106_bpt
	@p_Home_TextBox106_bpt.setter
	def p_Home_TextBox106_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox106_bpt"] = {}
		global default_state
		self._p_Home_TextBox106_bpt = TextBox(new_state, default_state["p_Home_TextBox106_bpt"])

	@property
	def p_Home_Image54_bpt(self):
		self._getter_access_tracker["p_Home_Image54_bpt"] = {}
		return self._p_Home_Image54_bpt
	@p_Home_Image54_bpt.setter
	def p_Home_Image54_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image54_bpt"] = {}
		global default_state
		self._p_Home_Image54_bpt = Image(new_state, default_state["p_Home_Image54_bpt"])

	@property
	def p_Home_TextBox107_bpt(self):
		self._getter_access_tracker["p_Home_TextBox107_bpt"] = {}
		return self._p_Home_TextBox107_bpt
	@p_Home_TextBox107_bpt.setter
	def p_Home_TextBox107_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox107_bpt"] = {}
		global default_state
		self._p_Home_TextBox107_bpt = TextBox(new_state, default_state["p_Home_TextBox107_bpt"])

	@property
	def p_Home_Image55_bpt(self):
		self._getter_access_tracker["p_Home_Image55_bpt"] = {}
		return self._p_Home_Image55_bpt
	@p_Home_Image55_bpt.setter
	def p_Home_Image55_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image55_bpt"] = {}
		global default_state
		self._p_Home_Image55_bpt = Image(new_state, default_state["p_Home_Image55_bpt"])

	@property
	def p_Home_TextBox111_bpt(self):
		self._getter_access_tracker["p_Home_TextBox111_bpt"] = {}
		return self._p_Home_TextBox111_bpt
	@p_Home_TextBox111_bpt.setter
	def p_Home_TextBox111_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox111_bpt"] = {}
		global default_state
		self._p_Home_TextBox111_bpt = TextBox(new_state, default_state["p_Home_TextBox111_bpt"])

	@property
	def p_Home_Image56_bpt(self):
		self._getter_access_tracker["p_Home_Image56_bpt"] = {}
		return self._p_Home_Image56_bpt
	@p_Home_Image56_bpt.setter
	def p_Home_Image56_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image56_bpt"] = {}
		global default_state
		self._p_Home_Image56_bpt = Image(new_state, default_state["p_Home_Image56_bpt"])

	@property
	def p_Home_TextBox112_bpt(self):
		self._getter_access_tracker["p_Home_TextBox112_bpt"] = {}
		return self._p_Home_TextBox112_bpt
	@p_Home_TextBox112_bpt.setter
	def p_Home_TextBox112_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox112_bpt"] = {}
		global default_state
		self._p_Home_TextBox112_bpt = TextBox(new_state, default_state["p_Home_TextBox112_bpt"])

	@property
	def p_Home_TextBox122_bpt(self):
		self._getter_access_tracker["p_Home_TextBox122_bpt"] = {}
		return self._p_Home_TextBox122_bpt
	@p_Home_TextBox122_bpt.setter
	def p_Home_TextBox122_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox122_bpt"] = {}
		global default_state
		self._p_Home_TextBox122_bpt = TextBox(new_state, default_state["p_Home_TextBox122_bpt"])

	@property
	def p_Home_TextBox121_bpt(self):
		self._getter_access_tracker["p_Home_TextBox121_bpt"] = {}
		return self._p_Home_TextBox121_bpt
	@p_Home_TextBox121_bpt.setter
	def p_Home_TextBox121_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox121_bpt"] = {}
		global default_state
		self._p_Home_TextBox121_bpt = TextBox(new_state, default_state["p_Home_TextBox121_bpt"])

	@property
	def p_Home_Image58_bpt(self):
		self._getter_access_tracker["p_Home_Image58_bpt"] = {}
		return self._p_Home_Image58_bpt
	@p_Home_Image58_bpt.setter
	def p_Home_Image58_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image58_bpt"] = {}
		global default_state
		self._p_Home_Image58_bpt = Image(new_state, default_state["p_Home_Image58_bpt"])

	@property
	def p_Home_Image59_bpt(self):
		self._getter_access_tracker["p_Home_Image59_bpt"] = {}
		return self._p_Home_Image59_bpt
	@p_Home_Image59_bpt.setter
	def p_Home_Image59_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image59_bpt"] = {}
		global default_state
		self._p_Home_Image59_bpt = Image(new_state, default_state["p_Home_Image59_bpt"])

	@property
	def p_Home_Image61_bpt(self):
		self._getter_access_tracker["p_Home_Image61_bpt"] = {}
		return self._p_Home_Image61_bpt
	@p_Home_Image61_bpt.setter
	def p_Home_Image61_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image61_bpt"] = {}
		global default_state
		self._p_Home_Image61_bpt = Image(new_state, default_state["p_Home_Image61_bpt"])

	@property
	def p_Home_Image60_bpt(self):
		self._getter_access_tracker["p_Home_Image60_bpt"] = {}
		return self._p_Home_Image60_bpt
	@p_Home_Image60_bpt.setter
	def p_Home_Image60_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image60_bpt"] = {}
		global default_state
		self._p_Home_Image60_bpt = Image(new_state, default_state["p_Home_Image60_bpt"])

	@property
	def p_Home_Image63_bpt(self):
		self._getter_access_tracker["p_Home_Image63_bpt"] = {}
		return self._p_Home_Image63_bpt
	@p_Home_Image63_bpt.setter
	def p_Home_Image63_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image63_bpt"] = {}
		global default_state
		self._p_Home_Image63_bpt = Image(new_state, default_state["p_Home_Image63_bpt"])

	@property
	def p_Home_Image62_bpt(self):
		self._getter_access_tracker["p_Home_Image62_bpt"] = {}
		return self._p_Home_Image62_bpt
	@p_Home_Image62_bpt.setter
	def p_Home_Image62_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image62_bpt"] = {}
		global default_state
		self._p_Home_Image62_bpt = Image(new_state, default_state["p_Home_Image62_bpt"])

	@property
	def p_Home_Image64_bpt(self):
		self._getter_access_tracker["p_Home_Image64_bpt"] = {}
		return self._p_Home_Image64_bpt
	@p_Home_Image64_bpt.setter
	def p_Home_Image64_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image64_bpt"] = {}
		global default_state
		self._p_Home_Image64_bpt = Image(new_state, default_state["p_Home_Image64_bpt"])

	@property
	def p_Home_TextBox123_bpt(self):
		self._getter_access_tracker["p_Home_TextBox123_bpt"] = {}
		return self._p_Home_TextBox123_bpt
	@p_Home_TextBox123_bpt.setter
	def p_Home_TextBox123_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox123_bpt"] = {}
		global default_state
		self._p_Home_TextBox123_bpt = TextBox(new_state, default_state["p_Home_TextBox123_bpt"])

	@property
	def p_Home_Image65_bpt(self):
		self._getter_access_tracker["p_Home_Image65_bpt"] = {}
		return self._p_Home_Image65_bpt
	@p_Home_Image65_bpt.setter
	def p_Home_Image65_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image65_bpt"] = {}
		global default_state
		self._p_Home_Image65_bpt = Image(new_state, default_state["p_Home_Image65_bpt"])

	@property
	def p_Home_Image66_bpt(self):
		self._getter_access_tracker["p_Home_Image66_bpt"] = {}
		return self._p_Home_Image66_bpt
	@p_Home_Image66_bpt.setter
	def p_Home_Image66_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image66_bpt"] = {}
		global default_state
		self._p_Home_Image66_bpt = Image(new_state, default_state["p_Home_Image66_bpt"])

	@property
	def p_Home_Image67_bpt(self):
		self._getter_access_tracker["p_Home_Image67_bpt"] = {}
		return self._p_Home_Image67_bpt
	@p_Home_Image67_bpt.setter
	def p_Home_Image67_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image67_bpt"] = {}
		global default_state
		self._p_Home_Image67_bpt = Image(new_state, default_state["p_Home_Image67_bpt"])

	@property
	def p_Home_Image68_bpt(self):
		self._getter_access_tracker["p_Home_Image68_bpt"] = {}
		return self._p_Home_Image68_bpt
	@p_Home_Image68_bpt.setter
	def p_Home_Image68_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image68_bpt"] = {}
		global default_state
		self._p_Home_Image68_bpt = Image(new_state, default_state["p_Home_Image68_bpt"])

	@property
	def p_Home_Image69_bpt(self):
		self._getter_access_tracker["p_Home_Image69_bpt"] = {}
		return self._p_Home_Image69_bpt
	@p_Home_Image69_bpt.setter
	def p_Home_Image69_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image69_bpt"] = {}
		global default_state
		self._p_Home_Image69_bpt = Image(new_state, default_state["p_Home_Image69_bpt"])

	@property
	def p_Home_TextBox125_bpt(self):
		self._getter_access_tracker["p_Home_TextBox125_bpt"] = {}
		return self._p_Home_TextBox125_bpt
	@p_Home_TextBox125_bpt.setter
	def p_Home_TextBox125_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox125_bpt"] = {}
		global default_state
		self._p_Home_TextBox125_bpt = TextBox(new_state, default_state["p_Home_TextBox125_bpt"])

	@property
	def p_Home_TextBox126_bpt(self):
		self._getter_access_tracker["p_Home_TextBox126_bpt"] = {}
		return self._p_Home_TextBox126_bpt
	@p_Home_TextBox126_bpt.setter
	def p_Home_TextBox126_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox126_bpt"] = {}
		global default_state
		self._p_Home_TextBox126_bpt = TextBox(new_state, default_state["p_Home_TextBox126_bpt"])

	@property
	def p_Home_TextBox127_bpt(self):
		self._getter_access_tracker["p_Home_TextBox127_bpt"] = {}
		return self._p_Home_TextBox127_bpt
	@p_Home_TextBox127_bpt.setter
	def p_Home_TextBox127_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox127_bpt"] = {}
		global default_state
		self._p_Home_TextBox127_bpt = TextBox(new_state, default_state["p_Home_TextBox127_bpt"])

	@property
	def p_Home_TextBox128_bpt(self):
		self._getter_access_tracker["p_Home_TextBox128_bpt"] = {}
		return self._p_Home_TextBox128_bpt
	@p_Home_TextBox128_bpt.setter
	def p_Home_TextBox128_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox128_bpt"] = {}
		global default_state
		self._p_Home_TextBox128_bpt = TextBox(new_state, default_state["p_Home_TextBox128_bpt"])

	@property
	def p_Home_TextBox129_bpt(self):
		self._getter_access_tracker["p_Home_TextBox129_bpt"] = {}
		return self._p_Home_TextBox129_bpt
	@p_Home_TextBox129_bpt.setter
	def p_Home_TextBox129_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox129_bpt"] = {}
		global default_state
		self._p_Home_TextBox129_bpt = TextBox(new_state, default_state["p_Home_TextBox129_bpt"])

	@property
	def p_Home_TextBox130_bpt(self):
		self._getter_access_tracker["p_Home_TextBox130_bpt"] = {}
		return self._p_Home_TextBox130_bpt
	@p_Home_TextBox130_bpt.setter
	def p_Home_TextBox130_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox130_bpt"] = {}
		global default_state
		self._p_Home_TextBox130_bpt = TextBox(new_state, default_state["p_Home_TextBox130_bpt"])

	@property
	def p_Home_TextBox131_bpt(self):
		self._getter_access_tracker["p_Home_TextBox131_bpt"] = {}
		return self._p_Home_TextBox131_bpt
	@p_Home_TextBox131_bpt.setter
	def p_Home_TextBox131_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox131_bpt"] = {}
		global default_state
		self._p_Home_TextBox131_bpt = TextBox(new_state, default_state["p_Home_TextBox131_bpt"])

	@property
	def p_Home_TextBox133_bpt(self):
		self._getter_access_tracker["p_Home_TextBox133_bpt"] = {}
		return self._p_Home_TextBox133_bpt
	@p_Home_TextBox133_bpt.setter
	def p_Home_TextBox133_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox133_bpt"] = {}
		global default_state
		self._p_Home_TextBox133_bpt = TextBox(new_state, default_state["p_Home_TextBox133_bpt"])

	@property
	def p_Home_TextBox134_bpt(self):
		self._getter_access_tracker["p_Home_TextBox134_bpt"] = {}
		return self._p_Home_TextBox134_bpt
	@p_Home_TextBox134_bpt.setter
	def p_Home_TextBox134_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox134_bpt"] = {}
		global default_state
		self._p_Home_TextBox134_bpt = TextBox(new_state, default_state["p_Home_TextBox134_bpt"])

	@property
	def p_Home_TextBox139_bpt(self):
		self._getter_access_tracker["p_Home_TextBox139_bpt"] = {}
		return self._p_Home_TextBox139_bpt
	@p_Home_TextBox139_bpt.setter
	def p_Home_TextBox139_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox139_bpt"] = {}
		global default_state
		self._p_Home_TextBox139_bpt = TextBox(new_state, default_state["p_Home_TextBox139_bpt"])

	@property
	def p_Home_TextBox138_bpt(self):
		self._getter_access_tracker["p_Home_TextBox138_bpt"] = {}
		return self._p_Home_TextBox138_bpt
	@p_Home_TextBox138_bpt.setter
	def p_Home_TextBox138_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox138_bpt"] = {}
		global default_state
		self._p_Home_TextBox138_bpt = TextBox(new_state, default_state["p_Home_TextBox138_bpt"])

	@property
	def p_Home_TextBox137_bpt(self):
		self._getter_access_tracker["p_Home_TextBox137_bpt"] = {}
		return self._p_Home_TextBox137_bpt
	@p_Home_TextBox137_bpt.setter
	def p_Home_TextBox137_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox137_bpt"] = {}
		global default_state
		self._p_Home_TextBox137_bpt = TextBox(new_state, default_state["p_Home_TextBox137_bpt"])

	@property
	def p_Home_TextBox136_bpt(self):
		self._getter_access_tracker["p_Home_TextBox136_bpt"] = {}
		return self._p_Home_TextBox136_bpt
	@p_Home_TextBox136_bpt.setter
	def p_Home_TextBox136_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox136_bpt"] = {}
		global default_state
		self._p_Home_TextBox136_bpt = TextBox(new_state, default_state["p_Home_TextBox136_bpt"])

	@property
	def p_Home_TextBox135_bpt(self):
		self._getter_access_tracker["p_Home_TextBox135_bpt"] = {}
		return self._p_Home_TextBox135_bpt
	@p_Home_TextBox135_bpt.setter
	def p_Home_TextBox135_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox135_bpt"] = {}
		global default_state
		self._p_Home_TextBox135_bpt = TextBox(new_state, default_state["p_Home_TextBox135_bpt"])

	@property
	def p_Home_TextBox140_bpt(self):
		self._getter_access_tracker["p_Home_TextBox140_bpt"] = {}
		return self._p_Home_TextBox140_bpt
	@p_Home_TextBox140_bpt.setter
	def p_Home_TextBox140_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox140_bpt"] = {}
		global default_state
		self._p_Home_TextBox140_bpt = TextBox(new_state, default_state["p_Home_TextBox140_bpt"])

	@property
	def p_Home_TextBox141_bpt(self):
		self._getter_access_tracker["p_Home_TextBox141_bpt"] = {}
		return self._p_Home_TextBox141_bpt
	@p_Home_TextBox141_bpt.setter
	def p_Home_TextBox141_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox141_bpt"] = {}
		global default_state
		self._p_Home_TextBox141_bpt = TextBox(new_state, default_state["p_Home_TextBox141_bpt"])

	@property
	def p_Home_TextBox124_bpt(self):
		self._getter_access_tracker["p_Home_TextBox124_bpt"] = {}
		return self._p_Home_TextBox124_bpt
	@p_Home_TextBox124_bpt.setter
	def p_Home_TextBox124_bpt(self, new_state):
		self._setter_access_tracker["p_Home_TextBox124_bpt"] = {}
		global default_state
		self._p_Home_TextBox124_bpt = TextBox(new_state, default_state["p_Home_TextBox124_bpt"])

	@property
	def p_Home_Image72_bpt(self):
		self._getter_access_tracker["p_Home_Image72_bpt"] = {}
		return self._p_Home_Image72_bpt
	@p_Home_Image72_bpt.setter
	def p_Home_Image72_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image72_bpt"] = {}
		global default_state
		self._p_Home_Image72_bpt = Image(new_state, default_state["p_Home_Image72_bpt"])

	@property
	def p_Home_Image73_bpt(self):
		self._getter_access_tracker["p_Home_Image73_bpt"] = {}
		return self._p_Home_Image73_bpt
	@p_Home_Image73_bpt.setter
	def p_Home_Image73_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image73_bpt"] = {}
		global default_state
		self._p_Home_Image73_bpt = Image(new_state, default_state["p_Home_Image73_bpt"])

	@property
	def p_Home_Image70_bpt(self):
		self._getter_access_tracker["p_Home_Image70_bpt"] = {}
		return self._p_Home_Image70_bpt
	@p_Home_Image70_bpt.setter
	def p_Home_Image70_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image70_bpt"] = {}
		global default_state
		self._p_Home_Image70_bpt = Image(new_state, default_state["p_Home_Image70_bpt"])

	@property
	def p_Home_Image71_bpt(self):
		self._getter_access_tracker["p_Home_Image71_bpt"] = {}
		return self._p_Home_Image71_bpt
	@p_Home_Image71_bpt.setter
	def p_Home_Image71_bpt(self, new_state):
		self._setter_access_tracker["p_Home_Image71_bpt"] = {}
		global default_state
		self._p_Home_Image71_bpt = Image(new_state, default_state["p_Home_Image71_bpt"])

	def _to_json_fields(self):
		return {
			"p_Home_Flex1_bpt": self._p_Home_Flex1_bpt,
			"p_Home_Flex2_bpt": self._p_Home_Flex2_bpt,
			"p_Home_Flex4_bpt": self._p_Home_Flex4_bpt,
			"p_Home_Flex138_bpt": self._p_Home_Flex138_bpt,
			"p_Home_TextBox1_bpt": self._p_Home_TextBox1_bpt,
			"p_Home_TextBox2_bpt": self._p_Home_TextBox2_bpt,
			"p_Home_TextBox6_bpt": self._p_Home_TextBox6_bpt,
			"p_Home_TextBox4_bpt": self._p_Home_TextBox4_bpt,
			"p_Home_TextBox3_bpt": self._p_Home_TextBox3_bpt,
			"p_Home_Flex3_bpt": self._p_Home_Flex3_bpt,
			"p_Home_Flex5_bpt": self._p_Home_Flex5_bpt,
			"p_Home_Flex6_bpt": self._p_Home_Flex6_bpt,
			"p_Home_TextBox9_bpt": self._p_Home_TextBox9_bpt,
			"p_Home_Flex8_bpt": self._p_Home_Flex8_bpt,
			"p_Home_Flex9_bpt": self._p_Home_Flex9_bpt,
			"p_Home_Flex10_bpt": self._p_Home_Flex10_bpt,
			"p_Home_TextBox7_bpt": self._p_Home_TextBox7_bpt,
			"p_Home_TextBox8_bpt": self._p_Home_TextBox8_bpt,
			"p_Home_Flex7_bpt": self._p_Home_Flex7_bpt,
			"p_Home_Flex11_bpt": self._p_Home_Flex11_bpt,
			"p_Home_Flex12_bpt": self._p_Home_Flex12_bpt,
			"p_Home_Flex371_bpt": self._p_Home_Flex371_bpt,
			"p_Home_Flex373_bpt": self._p_Home_Flex373_bpt,
			"p_Home_Flex13_bpt": self._p_Home_Flex13_bpt,
			"p_Home_Flex14_bpt": self._p_Home_Flex14_bpt,
			"p_Home_Flex365_bpt": self._p_Home_Flex365_bpt,
			"p_Home_Flex15_bpt": self._p_Home_Flex15_bpt,
			"p_Home_Flex366_bpt": self._p_Home_Flex366_bpt,
			"p_Home_Flex367_bpt": self._p_Home_Flex367_bpt,
			"p_Home_Flex21_bpt": self._p_Home_Flex21_bpt,
			"p_Home_Flex368_bpt": self._p_Home_Flex368_bpt,
			"p_Home_Flex25_bpt": self._p_Home_Flex25_bpt,
			"p_Home_Flex26_bpt": self._p_Home_Flex26_bpt,
			"p_Home_Flex27_bpt": self._p_Home_Flex27_bpt,
			"p_Home_Flex29_bpt": self._p_Home_Flex29_bpt,
			"p_Home_Flex30_bpt": self._p_Home_Flex30_bpt,
			"p_Home_Flex35_bpt": self._p_Home_Flex35_bpt,
			"p_Home_Flex32_bpt": self._p_Home_Flex32_bpt,
			"p_Home_Flex28_bpt": self._p_Home_Flex28_bpt,
			"p_Home_Flex37_bpt": self._p_Home_Flex37_bpt,
			"p__Home_Flex38_bpt": self._p__Home_Flex38_bpt,
			"p_Home_Flex39_bpt": self._p_Home_Flex39_bpt,
			"p_Home_Flex40_bpt": self._p_Home_Flex40_bpt,
			"p_Home_Flex297_bpt": self._p_Home_Flex297_bpt,
			"p_Home_Product_Card_1_bpt": self._p_Home_Product_Card_1_bpt,
			"p_Home_Flex42_bpt": self._p_Home_Flex42_bpt,
			"p_Home_Product_Card_2_bpt": self._p_Home_Product_Card_2_bpt,
			"p_Home_Flex43_bpt": self._p_Home_Flex43_bpt,
			"p_Home_Flex298_bpt": self._p_Home_Flex298_bpt,
			"p_Home_Product_Card_4_bpt": self._p_Home_Product_Card_4_bpt,
			"p_Home_Flex47_bpt": self._p_Home_Flex47_bpt,
			"p_Home_Product_Card_3_bpt": self._p_Home_Product_Card_3_bpt,
			"p_Home_Flex45_bpt": self._p_Home_Flex45_bpt,
			"p_Home_Flex58_bpt": self._p_Home_Flex58_bpt,
			"p_Home_Flex57_bpt": self._p_Home_Flex57_bpt,
			"p_Home_Flex300_bpt": self._p_Home_Flex300_bpt,
			"p_Home_Product_Card_7_bpt": self._p_Home_Product_Card_7_bpt,
			"p_Home_Flex50_bpt": self._p_Home_Flex50_bpt,
			"p_Home_Product_Card_8_bpt": self._p_Home_Product_Card_8_bpt,
			"p_Home_Flex49_bpt": self._p_Home_Flex49_bpt,
			"p_Home_Flex299_bpt": self._p_Home_Flex299_bpt,
			"p_Home_Product_Card_6_bpt": self._p_Home_Product_Card_6_bpt,
			"p_Home_Flex51_bpt": self._p_Home_Flex51_bpt,
			"p_Home_Product_Card_5_bpt": self._p_Home_Product_Card_5_bpt,
			"p_Home_Flex52_bpt": self._p_Home_Flex52_bpt,
			"p_Home_Flex59_bpt": self._p_Home_Flex59_bpt,
			"p_Home_Flex60_bpt": self._p_Home_Flex60_bpt,
			"p_Home_Flex62_bpt": self._p_Home_Flex62_bpt,
			"p_Home_Flex61_bpt": self._p_Home_Flex61_bpt,
			"p_Home_Flex63_bpt": self._p_Home_Flex63_bpt,
			"p_Home_Flex130_bpt": self._p_Home_Flex130_bpt,
			"p_Home_Flex89_bpt": self._p_Home_Flex89_bpt,
			"p_Home_Flex128_bpt": self._p_Home_Flex128_bpt,
			"p_Home_Flex64_bpt": self._p_Home_Flex64_bpt,
			"p_Home_Flex65_bpt": self._p_Home_Flex65_bpt,
			"p_Home_Flex131_bpt": self._p_Home_Flex131_bpt,
			"p_Home_Flex132_bpt": self._p_Home_Flex132_bpt,
			"p_Home_Flex133_bpt": self._p_Home_Flex133_bpt,
			"p_Home_Flex134_bpt": self._p_Home_Flex134_bpt,
			"p_Home_Flex1315_bpt": self._p_Home_Flex1315_bpt,
			"p_Home_Flex67_bpt": self._p_Home_Flex67_bpt,
			"p_Home_Flex68_bpt": self._p_Home_Flex68_bpt,
			"p_Home_Flex129_bpt": self._p_Home_Flex129_bpt,
			"p_Home_Flex69_bpt": self._p_Home_Flex69_bpt,
			"p_Home_Flex71_bpt": self._p_Home_Flex71_bpt,
			"p_Home_Flex72_bpt": self._p_Home_Flex72_bpt,
			"p_Home_Flex73_bpt": self._p_Home_Flex73_bpt,
			"p_Home_Flex74_bpt": self._p_Home_Flex74_bpt,
			"p_Home_Flex75_bpt": self._p_Home_Flex75_bpt,
			"p_Home_Flex76_bpt": self._p_Home_Flex76_bpt,
			"p_Home_Flex77_bpt": self._p_Home_Flex77_bpt,
			"p_Home_Flex81_bpt": self._p_Home_Flex81_bpt,
			"p_Home_Flex82_bpt": self._p_Home_Flex82_bpt,
			"p_Home_Flex85_bpt": self._p_Home_Flex85_bpt,
			"p_Home_Flex83_bpt": self._p_Home_Flex83_bpt,
			"p_Home_Flex84_bpt": self._p_Home_Flex84_bpt,
			"p_Home_Flex90_bpt": self._p_Home_Flex90_bpt,
			"p_Home_Flex92_bpt": self._p_Home_Flex92_bpt,
			"p_Home_Flex98_bpt": self._p_Home_Flex98_bpt,
			"p_Home_Flex99_bpt": self._p_Home_Flex99_bpt,
			"p_Home_Flex100_bpt": self._p_Home_Flex100_bpt,
			"p_Home_Flex101_bpt": self._p_Home_Flex101_bpt,
			"p_Home_Flex104_bpt": self._p_Home_Flex104_bpt,
			"p_Home_Flex103_bpt": self._p_Home_Flex103_bpt,
			"p_Home_Flex102_bpt": self._p_Home_Flex102_bpt,
			"p_Home_Flex107_bpt": self._p_Home_Flex107_bpt,
			"p_Home_Flex106_bpt": self._p_Home_Flex106_bpt,
			"p_Home_Flex105_bpt": self._p_Home_Flex105_bpt,
			"p_Home_Flex108_bpt": self._p_Home_Flex108_bpt,
			"p_Home_Flex91_bpt": self._p_Home_Flex91_bpt,
			"p_Home_Flex93_bpt": self._p_Home_Flex93_bpt,
			"p_Home_Flex94_bpt": self._p_Home_Flex94_bpt,
			"p_Home_Flex95_bpt": self._p_Home_Flex95_bpt,
			"p_Home_Flex110_bpt": self._p_Home_Flex110_bpt,
			"p_Home_Flex112_bpt": self._p_Home_Flex112_bpt,
			"p_Home_Flex111_bpt": self._p_Home_Flex111_bpt,
			"p_Home_Flex113_bpt": self._p_Home_Flex113_bpt,
			"p_Home_Flex114_bpt": self._p_Home_Flex114_bpt,
			"p_Home_Flex115_bpt": self._p_Home_Flex115_bpt,
			"p_Home_Flex116_bpt": self._p_Home_Flex116_bpt,
			"p_Home_Flex117_bpt": self._p_Home_Flex117_bpt,
			"p_Home_Flex118_bpt": self._p_Home_Flex118_bpt,
			"p_Home_Flex121_bpt": self._p_Home_Flex121_bpt,
			"p_Home_Flex119_bpt": self._p_Home_Flex119_bpt,
			"p_Home_Flex125_bpt": self._p_Home_Flex125_bpt,
			"p_Home_Flex127_bpt": self._p_Home_Flex127_bpt,
			"p_Home_Flex120_bpt": self._p_Home_Flex120_bpt,
			"p_Home_Flex124_bpt": self._p_Home_Flex124_bpt,
			"p_Home_Flex123_bpt": self._p_Home_Flex123_bpt,
			"p_Home_Flex122_bpt": self._p_Home_Flex122_bpt,
			"p_Home_Image2_bpt": self._p_Home_Image2_bpt,
			"TextBox4": self._TextBox4,
			"TextBox5": self._TextBox5,
			"TextBox8": self._TextBox8,
			"TextBox7": self._TextBox7,
			"TextBox6": self._TextBox6,
			"p_Home_Button1_bpt": self._p_Home_Button1_bpt,
			"p_Home_Button2_bpt": self._p_Home_Button2_bpt,
			"TextBox11": self._TextBox11,
			"p_Home_Button3_bpt": self._p_Home_Button3_bpt,
			"p_Home_Button4_bpt": self._p_Home_Button4_bpt,
			"TextBox9": self._TextBox9,
			"TextBox10": self._TextBox10,
			"p_Home_Image5_bpt": self._p_Home_Image5_bpt,
			"TextBox12": self._TextBox12,
			"p_Home_Image6_bpt": self._p_Home_Image6_bpt,
			"p_Home_Image10_bpt": self._p_Home_Image10_bpt,
			"p_Home_Image198_bpt": self._p_Home_Image198_bpt,
			"p_Home_Image197_bpt": self._p_Home_Image197_bpt,
			"p_Home_TextBox11_bpt": self._p_Home_TextBox11_bpt,
			"p_Home_Image11_bpt": self._p_Home_Image11_bpt,
			"p_Home_TextBox13_bpt": self._p_Home_TextBox13_bpt,
			"p_Home_TextBox14_bpt": self._p_Home_TextBox14_bpt,
			"p_Home_TextBox12_bpt": self._p_Home_TextBox12_bpt,
			"p_Home_Image195_bpt": self._p_Home_Image195_bpt,
			"p_Home_TextBox383_bpt": self._p_Home_TextBox383_bpt,
			"p_Home_TextBox384_bpt": self._p_Home_TextBox384_bpt,
			"p_Home_TextBox382_bpt": self._p_Home_TextBox382_bpt,
			"p_Home_TextBox32_bpt": self._p_Home_TextBox32_bpt,
			"p_Home_TextBox30_bpt": self._p_Home_TextBox30_bpt,
			"p_Home_TextBox31_bpt": self._p_Home_TextBox31_bpt,
			"p_Home_Image17_bpt": self._p_Home_Image17_bpt,
			"p_Home_Image196_bpt": self._p_Home_Image196_bpt,
			"p_Home_TextBox386_bpt": self._p_Home_TextBox386_bpt,
			"p_Home_TextBox387_bpt": self._p_Home_TextBox387_bpt,
			"p_Home_TextBox385_bpt": self._p_Home_TextBox385_bpt,
			"p_Home_Button9_bpt": self._p_Home_Button9_bpt,
			"p_Home_Button10_bpt": self._p_Home_Button10_bpt,
			"p_Home_Image19_bpt": self._p_Home_Image19_bpt,
			"p_Home_TextBox36_bpt": self._p_Home_TextBox36_bpt,
			"p_Home_Image20_bpt": self._p_Home_Image20_bpt,
			"p_Home_TextBox38_bpt": self._p_Home_TextBox38_bpt,
			"p_Home_Image25_bpt": self._p_Home_Image25_bpt,
			"p_Home_TextBox43_bpt": self._p_Home_TextBox43_bpt,
			"p_Home_Image22_bpt": self._p_Home_Image22_bpt,
			"p_Home_TextBox40_bpt": self._p_Home_TextBox40_bpt,
			"p_Home_TextBox44_bpt": self._p_Home_TextBox44_bpt,
			"p_Home_TextBox45_bpt": self._p_Home_TextBox45_bpt,
			"p_Home_TextBox46_bpt": self._p_Home_TextBox46_bpt,
			"p_Home_Button12_bpt": self._p_Home_Button12_bpt,
			"p_Home_Button11_bpt": self._p_Home_Button11_bpt,
			"p_Home_TextBox47_bpt": self._p_Home_TextBox47_bpt,
			"p_Home_TextBox48_bpt": self._p_Home_TextBox48_bpt,
			"p_Home_Product_Name_1_bpt": self._p_Home_Product_Name_1_bpt,
			"p_Home_Product_About_1_bpt": self._p_Home_Product_About_1_bpt,
			"p_Home_Product_Image_1_bpt": self._p_Home_Product_Image_1_bpt,
			"p_Home_Product_Price_1_bpt": self._p_Home_Product_Price_1_bpt,
			"p_Home_Product_Image_2_bpt": self._p_Home_Product_Image_2_bpt,
			"p_Home_Product_About_2_bpt": self._p_Home_Product_About_2_bpt,
			"p_Home_Product_Name_2_bpt": self._p_Home_Product_Name_2_bpt,
			"p_Home_Product_Price_2_bpt": self._p_Home_Product_Price_2_bpt,
			"p_Home_Product_Name_4_bpt": self._p_Home_Product_Name_4_bpt,
			"p_Home_Product_About_4_bpt": self._p_Home_Product_About_4_bpt,
			"p_Home_Product_Image_4_bpt": self._p_Home_Product_Image_4_bpt,
			"p_Home_Product_Price_4_bpt": self._p_Home_Product_Price_4_bpt,
			"p_Home_Product_Image_3_bpt": self._p_Home_Product_Image_3_bpt,
			"p_Home_Product_About_3_bpt": self._p_Home_Product_About_3_bpt,
			"p_Home_Product_Name_3_bpt": self._p_Home_Product_Name_3_bpt,
			"p_Home_Product_Price_3_bpt": self._p_Home_Product_Price_3_bpt,
			"p_Home_Button14_bpt": self._p_Home_Button14_bpt,
			"p_Home_Button13_bpt": self._p_Home_Button13_bpt,
			"p_Home_Product_Name_7_bpt": self._p_Home_Product_Name_7_bpt,
			"p_Home_Product_About_7_bpt": self._p_Home_Product_About_7_bpt,
			"p_Home_Product_Image_7_bpt": self._p_Home_Product_Image_7_bpt,
			"p_Home_Product_Price_7_bpt": self._p_Home_Product_Price_7_bpt,
			"p_Home_Product_Image_8_bpt": self._p_Home_Product_Image_8_bpt,
			"p_Home_Product_About_8_bpt": self._p_Home_Product_About_8_bpt,
			"p_Home_Product_Name_8_bpt": self._p_Home_Product_Name_8_bpt,
			"p_Home_Product_Price_8_bpt": self._p_Home_Product_Price_8_bpt,
			"p_Home_Product_Name_6_bpt": self._p_Home_Product_Name_6_bpt,
			"TextBox67": self._TextBox67,
			"p_Home_Product_Image_6_bpt": self._p_Home_Product_Image_6_bpt,
			"p_Home_Product_Price_6_bpt": self._p_Home_Product_Price_6_bpt,
			"p_Home_Product_Image_5_bpt": self._p_Home_Product_Image_5_bpt,
			"p_Home_Product_About_5_bpt": self._p_Home_Product_About_5_bpt,
			"p_Home_Product_Name_5_bpt": self._p_Home_Product_Name_5_bpt,
			"p_Home_Product_Price_5_bpt": self._p_Home_Product_Price_5_bpt,
			"p_Home_TextBox73_bpt": self._p_Home_TextBox73_bpt,
			"p_Home_TextBox74_bpt": self._p_Home_TextBox74_bpt,
			"p_Home_Button16_bpt": self._p_Home_Button16_bpt,
			"p_Home_Button15_bpt": self._p_Home_Button15_bpt,
			"p_Home_Image34_bpt": self._p_Home_Image34_bpt,
			"p_Home_TextBox75_bpt": self._p_Home_TextBox75_bpt,
			"p_Home_TextBox76_bpt": self._p_Home_TextBox76_bpt,
			"p_Home_TextBox142_bpt": self._p_Home_TextBox142_bpt,
			"p_Home_Image74_bpt": self._p_Home_Image74_bpt,
			"p_Home_TextBox78_bpt": self._p_Home_TextBox78_bpt,
			"p_Home_TextBox79_bpt": self._p_Home_TextBox79_bpt,
			"p_Home_Image44_bpt": self._p_Home_Image44_bpt,
			"p_Home_Image76_bpt": self._p_Home_Image76_bpt,
			"p_Home_Image77_bpt": self._p_Home_Image77_bpt,
			"p_Home_Image78_bpt": self._p_Home_Image78_bpt,
			"p_Home_Image79_bpt": self._p_Home_Image79_bpt,
			"p_Home_Image40_bpt": self._p_Home_Image40_bpt,
			"p_Home_TextBox81_bpt": self._p_Home_TextBox81_bpt,
			"p_Home_TextBox80_bpt": self._p_Home_TextBox80_bpt,
			"p_Home_Image75_bpt": self._p_Home_Image75_bpt,
			"p_Home_Button17_bpt": self._p_Home_Button17_bpt,
			"p_Home_Button18_bpt": self._p_Home_Button18_bpt,
			"p_Home_TextBox82_bpt": self._p_Home_TextBox82_bpt,
			"p_Home_TextBox83_bpt": self._p_Home_TextBox83_bpt,
			"p_Home_Image45_bpt": self._p_Home_Image45_bpt,
			"p_Home_TextBox85_bpt": self._p_Home_TextBox85_bpt,
			"p_Home_TextBox86_bpt": self._p_Home_TextBox86_bpt,
			"p_Home_TextBox84_bpt": self._p_Home_TextBox84_bpt,
			"p_Home_Image49_bpt": self._p_Home_Image49_bpt,
			"p_Home_TextBox97_bpt": self._p_Home_TextBox97_bpt,
			"p_Home_TextBox96_bpt": self._p_Home_TextBox96_bpt,
			"p_Home_TextBox100_bpt": self._p_Home_TextBox100_bpt,
			"p_Home_TextBox99": self._p_Home_TextBox99,
			"p_Home_Image51_bpt": self._p_Home_Image51_bpt,
			"p_Home_Image52_bpt": self._p_Home_Image52_bpt,
			"p_Home_TextBox102_bpt": self._p_Home_TextBox102_bpt,
			"p_Home_TextBox101_bpt": self._p_Home_TextBox101_bpt,
			"p_Home_TextBox104": self._p_Home_TextBox104,
			"p_Home_TextBox103_bpt": self._p_Home_TextBox103_bpt,
			"p_Home_Image53_bpt": self._p_Home_Image53_bpt,
			"p_Home_Button21_bpt": self._p_Home_Button21_bpt,
			"p_Home_TextBox113_bpt": self._p_Home_TextBox113_bpt,
			"p_Home_Input1_bpt": self._p_Home_Input1_bpt,
			"p_Home_Input2_bpt": self._p_Home_Input2_bpt,
			"p_Home_TextBox114_bpt": self._p_Home_TextBox114_bpt,
			"p_Home_Input4_bpt": self._p_Home_Input4_bpt,
			"p_Home_TextBox116_bpt": self._p_Home_TextBox116_bpt,
			"p_Home_Input3_bpt": self._p_Home_Input3_bpt,
			"p_Home_TextBox115_bpt": self._p_Home_TextBox115_bpt,
			"p_Home_TextBox118_bpt": self._p_Home_TextBox118_bpt,
			"p_Home_Input6_bpt": self._p_Home_Input6_bpt,
			"p_Home_TextBox117_bpt": self._p_Home_TextBox117_bpt,
			"p_Home_Input5_bpt": self._p_Home_Input5_bpt,
			"p_Home_TextBox120_bpt": self._p_Home_TextBox120_bpt,
			"p_Home_Input9_bpt": self._p_Home_Input9_bpt,
			"p_Home_TextBox105_bpt": self._p_Home_TextBox105_bpt,
			"p_Home_TextBox106_bpt": self._p_Home_TextBox106_bpt,
			"p_Home_Image54_bpt": self._p_Home_Image54_bpt,
			"p_Home_TextBox107_bpt": self._p_Home_TextBox107_bpt,
			"p_Home_Image55_bpt": self._p_Home_Image55_bpt,
			"p_Home_TextBox111_bpt": self._p_Home_TextBox111_bpt,
			"p_Home_Image56_bpt": self._p_Home_Image56_bpt,
			"p_Home_TextBox112_bpt": self._p_Home_TextBox112_bpt,
			"p_Home_TextBox122_bpt": self._p_Home_TextBox122_bpt,
			"p_Home_TextBox121_bpt": self._p_Home_TextBox121_bpt,
			"p_Home_Image58_bpt": self._p_Home_Image58_bpt,
			"p_Home_Image59_bpt": self._p_Home_Image59_bpt,
			"p_Home_Image61_bpt": self._p_Home_Image61_bpt,
			"p_Home_Image60_bpt": self._p_Home_Image60_bpt,
			"p_Home_Image63_bpt": self._p_Home_Image63_bpt,
			"p_Home_Image62_bpt": self._p_Home_Image62_bpt,
			"p_Home_Image64_bpt": self._p_Home_Image64_bpt,
			"p_Home_TextBox123_bpt": self._p_Home_TextBox123_bpt,
			"p_Home_Image65_bpt": self._p_Home_Image65_bpt,
			"p_Home_Image66_bpt": self._p_Home_Image66_bpt,
			"p_Home_Image67_bpt": self._p_Home_Image67_bpt,
			"p_Home_Image68_bpt": self._p_Home_Image68_bpt,
			"p_Home_Image69_bpt": self._p_Home_Image69_bpt,
			"p_Home_TextBox125_bpt": self._p_Home_TextBox125_bpt,
			"p_Home_TextBox126_bpt": self._p_Home_TextBox126_bpt,
			"p_Home_TextBox127_bpt": self._p_Home_TextBox127_bpt,
			"p_Home_TextBox128_bpt": self._p_Home_TextBox128_bpt,
			"p_Home_TextBox129_bpt": self._p_Home_TextBox129_bpt,
			"p_Home_TextBox130_bpt": self._p_Home_TextBox130_bpt,
			"p_Home_TextBox131_bpt": self._p_Home_TextBox131_bpt,
			"p_Home_TextBox133_bpt": self._p_Home_TextBox133_bpt,
			"p_Home_TextBox134_bpt": self._p_Home_TextBox134_bpt,
			"p_Home_TextBox139_bpt": self._p_Home_TextBox139_bpt,
			"p_Home_TextBox138_bpt": self._p_Home_TextBox138_bpt,
			"p_Home_TextBox137_bpt": self._p_Home_TextBox137_bpt,
			"p_Home_TextBox136_bpt": self._p_Home_TextBox136_bpt,
			"p_Home_TextBox135_bpt": self._p_Home_TextBox135_bpt,
			"p_Home_TextBox140_bpt": self._p_Home_TextBox140_bpt,
			"p_Home_TextBox141_bpt": self._p_Home_TextBox141_bpt,
			"p_Home_TextBox124_bpt": self._p_Home_TextBox124_bpt,
			"p_Home_Image72_bpt": self._p_Home_Image72_bpt,
			"p_Home_Image73_bpt": self._p_Home_Image73_bpt,
			"p_Home_Image70_bpt": self._p_Home_Image70_bpt,
			"p_Home_Image71_bpt": self._p_Home_Image71_bpt,
			}


class FlexstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.display: str = get_defined_value(state, def_state, "display")
		self.flexDirection: str = get_defined_value(state, def_state, "flexDirection")
		self.alignItems: str = get_defined_value(state, def_state, "alignItems")
		self.justifyContent: str = get_defined_value(state, def_state, "justifyContent")
		self.flexWrap: str = get_defined_value(state, def_state, "flexWrap")
		self.alignContent: str = get_defined_value(state, def_state, "alignContent")
		self.rowGap: str = get_defined_value(state, def_state, "rowGap")
		self.columnGap: str = get_defined_value(state, def_state, "columnGap")
		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def display(self):
		self._getter_access_tracker["display"] = {}
		return self._display
	@display.setter
	def display(self, state):
		self._setter_access_tracker["display"] = {}
		self._display = state
	@property
	def flexDirection(self):
		self._getter_access_tracker["flexDirection"] = {}
		return self._flexDirection
	@flexDirection.setter
	def flexDirection(self, state):
		self._setter_access_tracker["flexDirection"] = {}
		self._flexDirection = state
	@property
	def alignItems(self):
		self._getter_access_tracker["alignItems"] = {}
		return self._alignItems
	@alignItems.setter
	def alignItems(self, state):
		self._setter_access_tracker["alignItems"] = {}
		self._alignItems = state
	@property
	def justifyContent(self):
		self._getter_access_tracker["justifyContent"] = {}
		return self._justifyContent
	@justifyContent.setter
	def justifyContent(self, state):
		self._setter_access_tracker["justifyContent"] = {}
		self._justifyContent = state
	@property
	def flexWrap(self):
		self._getter_access_tracker["flexWrap"] = {}
		return self._flexWrap
	@flexWrap.setter
	def flexWrap(self, state):
		self._setter_access_tracker["flexWrap"] = {}
		self._flexWrap = state
	@property
	def alignContent(self):
		self._getter_access_tracker["alignContent"] = {}
		return self._alignContent
	@alignContent.setter
	def alignContent(self, state):
		self._setter_access_tracker["alignContent"] = {}
		self._alignContent = state
	@property
	def rowGap(self):
		self._getter_access_tracker["rowGap"] = {}
		return self._rowGap
	@rowGap.setter
	def rowGap(self, state):
		self._setter_access_tracker["rowGap"] = {}
		self._rowGap = state
	@property
	def columnGap(self):
		self._getter_access_tracker["columnGap"] = {}
		return self._columnGap
	@columnGap.setter
	def columnGap(self, state):
		self._setter_access_tracker["columnGap"] = {}
		self._columnGap = state
	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"display": self._display,
			"flexDirection": self._flexDirection,
			"alignItems": self._alignItems,
			"justifyContent": self._justifyContent,
			"flexWrap": self._flexWrap,
			"alignContent": self._alignContent,
			"rowGap": self._rowGap,
			"columnGap": self._columnGap,
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class Flex:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: FlexstylesClass = get_defined_value(state, def_state, "styles")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = FlexstylesClass(state, self._def_state["styles"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			}


class DivstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.display: str = get_defined_value(state, def_state, "display")
		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def display(self):
		self._getter_access_tracker["display"] = {}
		return self._display
	@display.setter
	def display(self, state):
		self._setter_access_tracker["display"] = {}
		self._display = state
	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"display": self._display,
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class Div:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: DivstylesClass = get_defined_value(state, def_state, "styles")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = DivstylesClass(state, self._def_state["styles"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			}


class ImagestylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class ImagecustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alt: str = get_defined_value(state, def_state, "alt")
		self.src: str = get_defined_value(state, def_state, "src")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alt(self):
		self._getter_access_tracker["alt"] = {}
		return self._alt
	@alt.setter
	def alt(self, state):
		self._setter_access_tracker["alt"] = {}
		self._alt = state
	@property
	def src(self):
		self._getter_access_tracker["src"] = {}
		return self._src
	@src.setter
	def src(self, state):
		self._setter_access_tracker["src"] = {}
		self._src = state
	def _to_json_fields(self):
		return {
			"alt": self._alt,
			"src": self._src,
			}


class Image:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: ImagestylesClass = get_defined_value(state, def_state, "styles")
		self.custom: ImagecustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = ImagestylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = ImagecustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}


class TextBoxstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class TextBoxcustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.text: str = get_defined_value(state, def_state, "text")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def text(self):
		self._getter_access_tracker["text"] = {}
		return self._text
	@text.setter
	def text(self, state):
		self._setter_access_tracker["text"] = {}
		self._text = state
	def _to_json_fields(self):
		return {
			"text": self._text,
			}


class TextBox:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: TextBoxstylesClass = get_defined_value(state, def_state, "styles")
		self.custom: TextBoxcustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = TextBoxstylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = TextBoxcustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}


class ButtonstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class ButtoncustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.text: str = get_defined_value(state, def_state, "text")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def text(self):
		self._getter_access_tracker["text"] = {}
		return self._text
	@text.setter
	def text(self, state):
		self._setter_access_tracker["text"] = {}
		self._text = state
	def _to_json_fields(self):
		return {
			"text": self._text,
			}


class Button:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: ButtonstylesClass = get_defined_value(state, def_state, "styles")
		self.custom: ButtoncustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = ButtonstylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = ButtoncustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}


class InputstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class InputcustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.value: str = get_defined_value(state, def_state, "value")
		self.placeholder: str = get_defined_value(state, def_state, "placeholder")
		self.isPasswordField: bool = get_defined_value(state, def_state, "isPasswordField")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def value(self):
		self._getter_access_tracker["value"] = {}
		return self._value
	@value.setter
	def value(self, state):
		self._setter_access_tracker["value"] = {}
		self._value = state
	@property
	def placeholder(self):
		self._getter_access_tracker["placeholder"] = {}
		return self._placeholder
	@placeholder.setter
	def placeholder(self, state):
		self._setter_access_tracker["placeholder"] = {}
		self._placeholder = state
	@property
	def isPasswordField(self):
		self._getter_access_tracker["isPasswordField"] = {}
		return self._isPasswordField
	@isPasswordField.setter
	def isPasswordField(self, state):
		self._setter_access_tracker["isPasswordField"] = {}
		self._isPasswordField = state
	def _to_json_fields(self):
		return {
			"value": self._value,
			"placeholder": self._placeholder,
			"isPasswordField": self._isPasswordField,
			}


class Input:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onChange = False
		self.onPressEnter = False
		self.styles: InputstylesClass = get_defined_value(state, def_state, "styles")
		self.custom: InputcustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = InputstylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = InputcustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}

