use crate::models::Politicalness;
use dioxus::prelude::*;

#[component]
pub(crate) fn PoliticalnessResult(
    politicalness: Option<Politicalness>,
    on_force_classify: EventHandler,
    display_force_classify: bool,
) -> Element {
    rsx! {
        div {
            class: "flex-grow flex flex-col h-32 md:h-auto",
            label {
                class: "px-4 flex flex-row justify-stretch font-semibold",
                r#for: "politicalness_result",
                span {
                    "Politicalness"
                }
                span {
                    class: "flex-grow text-right text-slate-500 font-normal",
                    "Existing model"
                }
            }
            div {
                id: "politicalness_result",
                class: format!(
                    "flex-grow p-4 flex flex-col justify-center items-center text-center {} font-semibold border shadow rounded-xl",
                    match politicalness {
                        None => "",
                        Some(Politicalness::Nonpolitical) => "bg-neutral-400 text-white",
                        Some(Politicalness::Political) => "bg-black text-white"
                    }
                ),
                match politicalness {
                    None => rsx! { "Processing..." },
                    Some(Politicalness::Nonpolitical) => rsx! {
                        div {
                            class: "flex flex-col gap-4",
                            p {
                                "The text is non-political."
                            }
                            if display_force_classify {
                                button {
                                    class: "py-4 px-5 bg-white text-neutral-400 font-semibold rounded-xl",
                                    onclick: move |_| {
                                        on_force_classify.call(());
                                    },
                                    "Classify anyway"
                                }
                            }
                        }
                    },
                    Some(Politicalness::Political) => rsx! { "The text is political." }
                }
            }
        }
    }
}
