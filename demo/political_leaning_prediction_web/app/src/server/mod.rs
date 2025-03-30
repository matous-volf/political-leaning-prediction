use crate::models::{PoliticalLeaning, Politicalness};
#[cfg(feature = "server")]
use crate::server::dotenv::DEEPL_API_KEY;
#[cfg(feature = "server")]
use deepl::reqwest::Client;
#[cfg(feature = "server")]
use deepl::{DeepLApi, Lang};
#[cfg(feature = "server")]
use dioxus::prelude::server_fn::error::NoCustomError;
use dioxus::prelude::*;
use serde::{Deserialize, Serialize};
#[cfg(feature = "server")]
use serde_json::json;

#[cfg(feature = "server")]
const MODEL_RUNNER_URL_BASE: &str = "http://model-runner:8001";
#[cfg(feature = "server")]
pub(crate) const MODEL_RUNNER_URL_POLITICALNESS: &str =
    constcat::concat!(MODEL_RUNNER_URL_BASE, "/politicalness");
#[cfg(feature = "server")]
pub(crate) const MODEL_RUNNER_URL_POLITICAL_LEANING: &str =
    constcat::concat!(MODEL_RUNNER_URL_BASE, "/political-leaning");

#[cfg(feature = "server")]
pub(crate) mod dotenv;

#[server]
pub(crate) async fn preprocess_text(text: String) -> Result<String, ServerFnError> {
    let deepl = DeepLApi::with(DEEPL_API_KEY).new();

    Ok(deepl
        .translate_text(text, Lang::EN)
        .await?
        .translations
        .pop()
        .ok_or(ServerFnError::WrappedServerError(NoCustomError))?
        .text)
}

#[allow(dead_code)]
#[derive(Deserialize, Debug)]
struct PoliticalnessResponse {
    result: String,
}

#[server]
pub(crate) async fn classify_text_by_politicalness(
    text: String,
) -> Result<Politicalness, ServerFnError> {
    let client = Client::new();

    let request_payload = json!({
        "text": text
    });

    let response = client
        .post(MODEL_RUNNER_URL_POLITICALNESS)
        .json(&request_payload)
        .send()
        .await?;

    response
        .json::<PoliticalnessResponse>()
        .await?
        .result
        .as_str()
        .try_into()
        .map_err(|_| ServerFnError::WrappedServerError(NoCustomError))
}

#[derive(Deserialize, Debug)]
struct PoliticalLeaningResponse {
    result: String,
    confidence: u8,
}

#[derive(PartialEq, Serialize, Deserialize, Clone, Debug)]
pub struct PoliticalLeaningWithConfidence {
    pub(crate) political_leaning: PoliticalLeaning,
    pub(crate) confidence: u8,
}

impl TryFrom<PoliticalLeaningResponse> for PoliticalLeaningWithConfidence {
    type Error = ();

    fn try_from(political_leaning_response: PoliticalLeaningResponse) -> Result<Self, Self::Error> {
        Ok(Self {
            political_leaning: political_leaning_response.result.as_str().try_into()?,
            confidence: political_leaning_response.confidence,
        })
    }
}

#[server]
pub(crate) async fn classify_text_by_political_leaning(
    text: String,
) -> Result<PoliticalLeaningWithConfidence, ServerFnError> {
    let client = Client::new();

    let request_payload = json!({
        "text": text
    });

    let response = client
        .post(MODEL_RUNNER_URL_POLITICAL_LEANING)
        .json(&request_payload)
        .send()
        .await?;

    response
        .json::<PoliticalLeaningResponse>()
        .await?
        .try_into()
        .map_err(|_| ServerFnError::WrappedServerError(NoCustomError))
}
