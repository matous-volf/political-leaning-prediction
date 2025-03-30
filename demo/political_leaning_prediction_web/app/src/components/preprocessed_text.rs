use dioxus::prelude::*;

#[component]
pub(crate) fn PreprocessedText(text: Option<String>) -> Element {
    rsx! {
        div {
            class: "flex-grow h-64 md:h-auto md:min-h-0 flex flex-col max-h-[300px]",
            label {
                class: "px-4 flex flex-row justify-stretch font-semibold",
                r#for: "preprocessed_text",
                span {
                    "Překlad"
                }
                span {
                    class: "flex-grow text-right text-slate-500 font-normal",
                    "DeepL"
                }
            }
            p {
                id: "preprocessed_text",
                class: "p-4 flex-grow font-medium border shadow rounded-xl overflow-y-scroll whitespace-pre-wrap",
                match text {
                    None => rsx!{
                        div {
                            class: "animate-pulse flex space-x-4",
                            div {
                                class: "flex-1 space-y-6 py-1",
                                div {
                                    class: "h-4 bg-slate-300 rounded",
                                }
                                div {
                                    class: "space-y-3",
                                    div {
                                        class: "grid grid-cols-3 gap-4",
                                        div {
                                            class: "h-4 bg-slate-300 rounded col-span-2",
                                        }
                                        div {
                                            class: "h-4 bg-slate-300 rounded col-span-1",
                                        }
                                    }
                                    div {
                                        class: "h-4 bg-slate-300 rounded",
                                    }
                                    div {
                                        class: "grid grid-cols-3 gap-4",
                                        div {
                                            class: "h-4 bg-slate-300 rounded col-span-1",
                                        }
                                        div {
                                            class: "h-4 bg-slate-300 rounded col-span-2",
                                        }
                                    }
                                }
                                div {
                                    class: "grid grid-cols-3 gap-4",
                                    div {
                                        class: "h-4 bg-slate-300 rounded col-span-2",
                                    }
                                }
                            }
                        }
                    },
                    Some(text) => rsx! {
                        {text}
                    }
                }
            }
        }
    }
}
