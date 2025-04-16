use crate::components::{InputText, PoliticalLeaningResult, PoliticalnessResult, PreprocessedText};
use crate::models::Politicalness;
use crate::server::{
    classify_text_by_political_leaning, classify_text_by_politicalness, preprocess_text,
};
use dioxus::prelude::*;

#[component]
pub(crate) fn Home() -> Element {
    let mut has_classified_once = use_signal(|| false);
    let mut preprocessed_text = use_signal::<Option<Option<String>>>(|| None);
    let mut politicalness = use_signal::<Option<Option<Politicalness>>>(|| None);
    let mut political_leaning = use_signal(|| None);

    rsx! {
        main {
            class: "flex-grow flex flex-col items-center gap-8",
            h1 {
                class: "text-center text-3xl font-semibold",
                "Political leaning classifier"
            }
            div {
                class: format!(
                    "flex-grow self-center w-full max-w-[1024px] flex flex-col md:grid md:grid-rows-1 md:grid-flow-col md:justify-center gap-16 {} md:transition-[grid-template-columns,_gap,_padding] md:duration-1000 md:ease-in-out",
                    if has_classified_once() { "md:grid-cols-[0.5fr_0.5fr] md:gap-8 md:px-0" } else { "md:grid-cols-[0.5fr_0fr] md:gap-0 md:px-4" },
                ),
                form {
                    class: "flex flex-col gap-6",
                    onsubmit: move |event| async move {
                        if !has_classified_once() {
                            has_classified_once.set(true);
                            async_std::task::sleep(std::time::Duration::from_millis(500)).await;
                        }

                        politicalness.set(None);
                        political_leaning.set(None);

                        let input_text = event.values().get("text").unwrap().as_value();

                        preprocessed_text.set(Some(None));
                        let preprocessed_text_new = preprocess_text(input_text).await.unwrap();
                        async_std::task::sleep(std::time::Duration::from_millis(500)).await;
                        preprocessed_text.set(Some(Some(preprocessed_text_new.to_owned())));

                        politicalness.set(Some(None));
                        let politicalness_new = classify_text_by_politicalness(
                            preprocessed_text_new.clone()
                        ).await.unwrap();
                        politicalness.set(Some(Some(politicalness_new.clone())));

                        if politicalness_new == Politicalness::Nonpolitical {
                            return;
                        }

                        political_leaning.set(Some(None));
                        let political_leaning_new = classify_text_by_political_leaning(
                            preprocessed_text_new
                        ).await.unwrap();
                        political_leaning.set(Some(Some(political_leaning_new)));
                    },
                    InputText {}
                    button {
                        class: "py-4 px-5 bg-gradient-to-r from-[#266bb9] to-[#eb344b] text-white font-semibold rounded-xl shadow-md transition-[box-shadow] duration-300 hover:shadow-lg focus:shadow-none",
                        "Classify"
                    }
                }
                div {
                    class: "grid grid-rows-4 gap-6",
                    if let Some(preprocessed_text) = preprocessed_text() {
                        div {
                            class: "row-span-2 flex flex-col",
                            PreprocessedText {
                                text: preprocessed_text
                            }
                        }
                    }
                    if let Some(politicalness) = &politicalness() {
                        div {
                            class: format!(
                                "{} flex flex-col",
                                if *politicalness == Some(Politicalness::Nonpolitical) && political_leaning().is_none() {
                                    "row-span-2"
                                } else {
                                    ""
                                }
                            ),
                            PoliticalnessResult {
                                politicalness: politicalness.clone(),
                                on_force_classify: move |_| async move {
                                    political_leaning.set(Some(None));
                                    let political_leaning_new = classify_text_by_political_leaning(
                                        preprocessed_text().unwrap().unwrap()
                                    ).await.unwrap();
                                    political_leaning.set(Some(Some(political_leaning_new)));
                                },
                                display_force_classify: political_leaning().is_none()
                            }
                        }
                    }
                    if let Some(political_leaning_with_confidence) = political_leaning() {
                        PoliticalLeaningResult {
                            political_leaning_with_confidence,
                        }
                    }
                }
            }
        }
    }
}
