use crate::models::PoliticalLeaning;
use crate::server::PoliticalLeaningWithConfidence;
use dioxus::prelude::*;

#[component]
pub(crate) fn PoliticalLeaningResult(
    political_leaning_with_confidence: Option<PoliticalLeaningWithConfidence>,
) -> Element {
    rsx! {
        div {
            class: "flex flex-col h-32 md:h-auto",
            label {
                class: "ps-4 font-semibold",
                r#for: "political_leaning_result",
                "Political leaning"
            }
            div {
                id: "political_leaning_result",
                class: format!(
                    "flex-grow p-4 flex flex-col justify-center items-center text-center {} font-semibold border shadow rounded-xl",
                    match political_leaning_with_confidence {
                        None => "",
                        Some(PoliticalLeaningWithConfidence { political_leaning, .. })
                        => match political_leaning {
                            PoliticalLeaning::Left => "bg-[#266bb9] text-white",
                            PoliticalLeaning::Center => "bg-[#70968e] text-white",
                            PoliticalLeaning::Right => "bg-[#eb344b] text-white",
                        }
                    }
                ),
                {
                    match &political_leaning_with_confidence {
                        None => rsx! { "Processing..." },
                        Some(PoliticalLeaningWithConfidence { political_leaning, confidence }) => rsx! {
                            p {
                                {format!(
                                    "The text supports the {}.",
                                    match political_leaning {
                                        PoliticalLeaning::Left => "left",
                                        PoliticalLeaning::Center => "center",
                                        PoliticalLeaning::Right => "right",
                                    }
                                )}
                            }
                            p {
                                class: "font-medium",
                                "Confidence: {confidence} %"
                            }
                        }
                    }
                }
            }
        }
    }
}
